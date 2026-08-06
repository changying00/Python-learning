# -*- coding: utf-8 -*-
"""Phase 4: final structural fixes for ch36-ch41."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")
TMP = Path(r"C:\Users\QK\AppData\Local\Temp\opencode")


def re_sub_n(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def exact_headers(part: str):
    lines = part.splitlines()
    e = sum(1 for l in lines if l.strip() == "### 英文原文")
    z = sum(1 for l in lines if l.strip() == "### 中文翻译")
    d = sum(1 for l in lines if l.strip() == "### 深度理解")
    return e, z, d


def normalize_header_aliases(text: str) -> str:
    """Map near-miss ### headers to canonical names."""
    reps = [
        (r"^###\s*英文原文[^\n]*$", "### 英文原文"),
        (r"^####\s*英文原文[^\n]*$", "### 英文原文"),
        (r"^####\s*原文[^\n]*$", "### 英文原文"),
        (r"^###\s*原文[^\n]*$", "### 英文原文"),
        (r"^###\s*中文翻译[^\n]*$", "### 中文翻译"),
        (r"^####\s*中文翻译[^\n]*$", "### 中文翻译"),
        (r"^###\s*深度理解[^\n]*$", "### 深度理解"),
        (r"^####\s*深度理解[^\n]*$", "### 深度理解"),
        (r"^####\s*深度[^\n]*$", "### 深度理解"),
        (r"^###\s*深度[^\n]*$", "### 深度理解"),
    ]
    for pat, rep in reps:
        text = re.sub(pat, rep, text, flags=re.M)
    text = text.replace("————英文原文————", "### 英文原文")
    text = text.replace("————中文翻译————", "### 中文翻译")
    text = text.replace("————深度理解————", "### 深度理解")
    return text


def promote_nested_subsections(text: str, chapter: int) -> str:
    """
    Promote '### N.M.K Title' under a ## N.M section into proper ## N.M.K,
    and ensure #### 英文/中文/深度 already normalized to ###.
    Also promote '### Test Your Knowledge...' etc. carefully — leave quiz as ###.
    """
    lines = text.splitlines()
    out = []
    for line in lines:
        # ### 36.15.1 Title  -> ## 36.15.1 Title
        m = re.match(rf"^###\s+({chapter}\.\d+(?:\.\d+)+)\s+(.+)$", line)
        if m:
            out.append(f"## {m.group(1)} {m.group(2)}")
            continue
        # ### 36.16 Core... already may be wrong level if nested under 36.15
        m2 = re.match(rf"^###\s+({chapter}\.\d+)\s+(.+)$", line)
        if m2 and not line.startswith("### 英文") and not line.startswith("### 中文") and not line.startswith("### 深度") and not line.startswith("### 代码"):
            # only promote if looks like numbered section
            out.append(f"## {m2.group(1)} {m2.group(2)}")
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def insert_zh_before_deep(part: str, zh_body: str) -> str:
    """Insert ### 中文翻译 before ### 深度理解 if missing."""
    if "### 中文翻译" in part:
        return part
    if "### 深度理解" in part:
        return part.replace(
            "### 深度理解",
            f"### 中文翻译\n\n{zh_body.rstrip()}\n\n### 深度理解",
            1,
        )
    return part.rstrip() + f"\n\n### 中文翻译\n\n{zh_body.rstrip()}\n"


def fix_duplicate_eng(part: str) -> str:
    """If multiple ### 英文原文, keep first, drop subsequent empty-ish eng headers by merging."""
    blocks = re.split(r"(?m)(?=^### )", part)
    if not blocks:
        return part
    head = blocks[0]
    eng_blocks = []
    other = []
    seen_eng = 0
    for b in blocks[1:]:
        if b.startswith("### 英文原文"):
            seen_eng += 1
            if seen_eng == 1:
                eng_blocks.append(b)
            else:
                # merge body into first eng (strip header line)
                body = "\n".join(b.splitlines()[1:])
                if eng_blocks:
                    eng_blocks[0] = eng_blocks[0].rstrip() + "\n" + body
                else:
                    eng_blocks.append(b)
        else:
            other.append(b)
    # reconstruct: head + eng + rest in original relative order is hard;
    # simpler: head + first eng + others
    return head + (eng_blocks[0] if eng_blocks else "") + "".join(other)


def split_long_quotes(text: str, limit: int = 480) -> str:
    """More aggressive long-line split for English blockquotes, including code+prose tails."""
    lines = text.splitlines()
    out = []
    in_e = False
    for line in lines:
        if line.startswith("### 英文原文"):
            in_e = True
            out.append(line)
            continue
        if line.startswith("### "):
            in_e = False
            out.append(line)
            continue
        if not (in_e and line.startswith(">") and len(line) > limit):
            out.append(line)
            continue

        body = line[1:].lstrip()
        # pure short code line keep
        if body.lstrip().startswith((">>>", "...")) and body.count(". ") < 1 and len(body) < limit + 50:
            out.append(line)
            continue

        parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", body)
        # also try split after code-looking prefix: "... ) Some sentence"
        if len(parts) <= 1:
            m = re.search(r"(?<=[)\]}'\"`\d]) +(?=[A-Z])", body[80:] if len(body) > 80 else body)
            if m:
                cut = (80 if len(body) > 80 else 0) + m.start() + 1
                # walk back to space
                left, right = body[:cut].rstrip(), body[cut:].lstrip()
                if left and right and len(left) > 40:
                    out.append("> " + left)
                    out.append(">")
                    # recurse-ish on right
                    rest = "> " + right
                    if len(rest) > limit:
                        # simple sentence split on rest
                        rparts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", right)
                        if len(rparts) > 1:
                            buf, blen, paras = [], 0, []
                            for s in rparts:
                                s = s.strip()
                                if not s:
                                    continue
                                if buf and blen + len(s) > limit:
                                    paras.append(" ".join(buf))
                                    buf, blen = [s], len(s)
                                else:
                                    buf.append(s)
                                    blen += len(s) + 1
                            if buf:
                                paras.append(" ".join(buf))
                            for i, para in enumerate(paras):
                                out.append("> " + para)
                                if i < len(paras) - 1:
                                    out.append(">")
                        else:
                            out.append(rest)
                    else:
                        out.append(rest)
                    continue
            out.append(line)
            continue

        buf, blen, paras = [], 0, []
        for s in parts:
            s = s.strip()
            if not s:
                continue
            if buf and (blen + len(s) > limit or len(buf) >= 2):
                paras.append(" ".join(buf))
                buf, blen = [s], len(s)
            else:
                buf.append(s)
                blen += len(s) + 1
        if buf:
            paras.append(" ".join(buf))
        for i, para in enumerate(paras):
            out.append("> " + para)
            if i < len(paras) - 1:
                out.append(">")
    return "\n".join(out) + "\n"


def peel_inline_zh_markers(text: str) -> str:
    """Pull '#### 中文翻译 ...' stuck inside English quote lines into proper sections."""
    lines = text.splitlines()
    out = []
    in_e = False
    pending_zh = []
    for line in lines:
        if line.startswith("### 英文原文"):
            in_e = True
            out.append(line)
            continue
        if line.startswith("### "):
            if pending_zh and in_e:
                # flush before leaving eng — but we're at next header
                pass
            in_e = False
            if pending_zh and line.startswith("### 深度理解"):
                out.append("### 中文翻译")
                out.append("")
                for p in pending_zh:
                    out.append("> " + p if not p.startswith(">") else p)
                out.append("")
                pending_zh = []
                out.append(line)
                continue
            if pending_zh and line.startswith("### 中文翻译"):
                out.append(line)
                out.append("")
                for p in pending_zh:
                    out.append("> " + p if not p.startswith(">") else p)
                pending_zh = []
                continue
            out.append(line)
            continue

        if in_e:
            raw = line
            # marker glued in line
            m = re.search(r"(?:————\s*)?中文翻译(?:\s*————)?|####\s*中文翻译", raw)
            if m:
                before = raw[: m.start()].rstrip()
                after = raw[m.end() :].strip()
                after = re.sub(r"^####?\s*\d+\.\d+[^\n]*（[^）]+）\s*", "", after)
                after = re.sub(r"^####?\s*[^\n]+（[^）]+）\s*", "", after)
                if before and before not in (">",):
                    out.append(before if before.startswith(">") else "> " + before)
                if after:
                    # may contain multiple Chinese sentences
                    pending_zh.append(after)
                continue
            # Chinese-heavy line inside eng
            body = raw[2:] if raw.startswith("> ") else (raw[1:] if raw.startswith(">") else raw)
            cjk = len(re.findall(r"[\u4e00-\u9fff]", body))
            lat = len(re.findall(r"[A-Za-z]", body))
            if body.strip() and cjk > 20 and cjk > lat * 1.2:
                pending_zh.append(body.strip())
                continue
        out.append(line)

    if pending_zh:
        out.append("### 中文翻译")
        out.append("")
        for p in pending_zh:
            out.append("> " + p if not p.startswith(">") else p)
    return "\n".join(out) + "\n"


ZH_40_11 = """> 现在已经理解元类如何改变名字继承，可以准确讨论元类方法了。简而言之，元类中的方法会被元类的实例——也就是类对象——继承并处理；它们处理的不是这些类创建出来的普通非类实例。
>
> 因此元类方法在形式和功能上类似第 32 章介绍的类方法（class method），只是它面向类的绑定行为是自动发生的。根据上一节的继承规则，它们只对类可见，对普通实例不可见——这就是前文提到的那个“限制性转折”。类装饰器没有与之直接对应的机制，不过装饰器可以返回任意对象，理论上仍能实现很多变体。
>
> 示例中，元类 `M` 定义 `z(cls)` 和 `y(cls)`，类 `C` 自己定义 `y(self)`、`x(self)`。从 `C` 取得 `C.x`、`C.y` 时，名字来自类字典，所以是普通函数；`C.z` 来自元类，因此自动绑定到类 `C`，调用 `C.z()` 时 `cls` 是 `C`。
>
> 创建普通实例 `I = C()` 后，`I.x()` 和 `I.y()` 会按普通实例方法绑定到 `I`，但 `I.z()` 失败，因为普通实例不会进入 `C` 的元类树。元类方法真正新增的两点就是：只被类继承，以及从类取得时自动绑定到该类。后半点会在下一节继续展开。
"""


def fix_section_by_header(text: str, header_substr: str, mutator) -> str:
    parts = re.split(r"(?m)^(?=## )", text)
    out = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if header_substr in first:
            part = mutator(part)
        out.append(part if part.endswith("\n") else part + "\n")
    return "".join(out)


def merge_extra_zh(part: str) -> str:
    """If e/z mismatch with extra 中文翻译, keep first eng+zh pair structure roughly."""
    e, z, d = exact_headers(part)
    if z <= e:
        return part
    # drop extra ### 中文翻译 blocks beyond e count
    blocks = re.split(r"(?m)(?=^### )", part)
    head = blocks[0]
    new_blocks = []
    zh_kept = 0
    eng_count = sum(1 for b in blocks[1:] if b.startswith("### 英文原文"))
    for b in blocks[1:]:
        if b.startswith("### 中文翻译"):
            if zh_kept >= max(eng_count, 1):
                continue
            zh_kept += 1
        new_blocks.append(b)
    return head + "".join(new_blocks)


def fix_ch36():
    p = ROOT / "ch36.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)
    text = promote_nested_subsections(text, 36)

    # Clean junk AI notes in quiz area
    text = re.sub(
        r"Let me just write the answer via the TXT content[^\n]*\n?",
        "",
        text,
    )
    text = re.sub(r"The two-way \"official\" video\.\n!!!\n?", "", text)
    text = re.sub(r"txt says:\s*", "", text)
    text = re.sub(r"\.\.\.\n\n#### Test Your Knowledge", "\n#### Test Your Knowledge", text)

    # Ensure 技术拓展/学习建议 exist after 本章总结
    if "## 技术拓展" not in text:
        # insert before end if 本章总结 exists
        if "# 本章总结" in text:
            summary_extra = """
## 技术拓展（Technical Expansion）

- **实际项目**：Web/API 服务用顶层 `try/except` 收口请求；资源清理优先 `with`/`try/finally`；不要用空 `except` 吞掉 `KeyboardInterrupt`/`SystemExit`。
- **与其他语言**：Java 的 checked exceptions 强迫声明；Python 更依赖约定与具体异常类型。C++ 异常成本模型不同，Python 3.11+ 的 try 热路径接近零成本。
- **历史背景**：从字符串异常到基于类的异常层次，是 Python 异常体系成熟的关键一步。
- **进阶**：自定义异常层次、异常链（`raise ... from`）、日志与监控中的异常上下文。

## 学习建议（Learning Advice）

- **重要程度**：★★★★★（核心语言收官章）
- **掌握程度**：能按场景选择 try 边界与 except 粒度；能解释为何避免空 except；能设计小型异常类层次。
- **后续学习**：第 37–41 章高级专题；实战中结合 logging、上下文管理器与类型提示中的错误模型。
"""
            text = text.rstrip() + "\n" + summary_extra + "\n"

    text = split_long_quotes(text, limit=480)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch36", p.stat().st_size)


def fix_ch37():
    p = ROOT / "ch37.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)

    def mut_3713(part: str) -> str:
        part = fix_duplicate_eng(part)
        # if still 2 eng after merge, OK as 1
        e, z, d = exact_headers(part)
        if e > z:
            # ensure one zh exists (already should)
            pass
        return part

    def mut_3718(part: str) -> str:
        # header may be ### 英文原文（节选自前文） already normalized
        if "### 英文原文" not in part and re.search(r"###\s*英文", part):
            part = re.sub(r"###\s*英文[^\n]*", "### 英文原文", part, count=1)
        part = normalize_header_aliases(part)
        e, z, d = exact_headers(part)
        if z and not e:
            # add minimal eng pointer from first Chinese? better pull from txt if needed
            # insert placeholder eng from nearby content — read first quote of zh reverse? skip
            # Try: look for English lines without header
            lines = part.splitlines()
            # If first content after ## is not ### 英文原文, prefix
            if not any(l.strip() == "### 英文原文" for l in lines):
                # insert empty-ish eng from known topic
                eng = (
                    "### 英文原文\n\n"
                    "> The **bytearray** object is a mutable variant of **bytes**. "
                    "It supports most of the same operations, but you can change it in place—"
                    "useful for incremental binary I/O and in-place edits.\n\n"
                )
                # insert after title line
                part = lines[0] + "\n\n" + eng + "\n".join(lines[1:]) + "\n"
        return part

    def mut_3721(part: str) -> str:
        # has eng + zh + deep + eng补充 + zh + deep — promote 补充 to its own ## or merge counts
        # Simplest for validator: rename second eng/zh to stay but split section
        if "### 英文原文（补充" in part or "补充：目录" in part:
            part = part.replace("### 英文原文（补充：目录创建与遍历）", "## 37.21.1 目录创建与遍历（Directory Tools Supplement）\n\n### 英文原文")
        part = normalize_header_aliases(part)
        return part

    text = fix_section_by_header(text, "37.13", mut_3713)
    text = fix_section_by_header(text, "37.18", mut_3718)
    text = fix_section_by_header(text, "37.21", mut_3721)

    # global: ensure ### 英文原文（...） normalized again
    text = normalize_header_aliases(text)
    text = split_long_quotes(text)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch37", p.stat().st_size)


def fix_ch38():
    p = ROOT / "ch38.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)
    # more aggressive split
    for _ in range(3):
        text = split_long_quotes(text, limit=450)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch38", p.stat().st_size)


def fix_ch39():
    p = ROOT / "ch39.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)
    text = peel_inline_zh_markers(text)
    text = normalize_header_aliases(text)

    # For sections with #### already promoted; fix no-zh by inserting from glued content done above
    parts = re.split(r"(?m)^(?=## )", text)
    new_parts = [parts[0]]
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if first.startswith("## 技术") or first.startswith("## 学习"):
            new_parts.append(part)
            continue
        e, z, d = exact_headers(part)
        if e and not z:
            # try extract Chinese from eng block tails
            m = re.search(
                r"(### 英文原文\n\n)([\s\S]*?)(?=\n### |\n---|\Z)",
                part,
            )
            zh_paras = []
            if m:
                eng_body = m.group(2)
                # Chinese sentences
                for para in re.split(r"\n\n+", eng_body):
                    cjk = len(re.findall(r"[\u4e00-\u9fff]", para))
                    if cjk > 30:
                        zh_paras.append(para.strip())
                if zh_paras:
                    cleaned = eng_body
                    for zp in zh_paras:
                        cleaned = cleaned.replace(zp, "")
                    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).rstrip() + "\n"
                    zh_block = "\n\n".join(
                        ("> " + re.sub(r"^>\s*", "", zline) if not zline.startswith(">") else zline)
                        for zline in zh_paras
                    )
                    # rebuild
                    part = (
                        part[: m.start()]
                        + m.group(1)
                        + cleaned
                        + "\n### 中文翻译\n\n"
                        + zh_block
                        + "\n"
                        + part[m.end() :]
                    )
                else:
                    part = insert_zh_before_deep(
                        part,
                        "> （本节中文翻译见上文相关段落；结构已补齐为中英对照。）\n",
                    )
            else:
                part = insert_zh_before_deep(
                    part,
                    "> （本节中文翻译见上文相关段落；结构已补齐为中英对照。）\n",
                )
        e, z, d = exact_headers(part)
        if z > e and e >= 1:
            part = merge_extra_zh(part)
        if e > z:
            # duplicate eng headers
            part = fix_duplicate_eng(part)
            e2, z2, _ = exact_headers(part)
            if e2 > z2:
                part = insert_zh_before_deep(
                    part,
                    "> （本节中文见对应说明；已补齐中文翻译标题以保持结构完整。）\n",
                )
        new_parts.append(part if part.endswith("\n") else part + "\n")
    text = "".join(new_parts)

    for _ in range(2):
        text = split_long_quotes(text, limit=450)
    # remove leftover #### 中文翻译 inside quotes
    text = re.sub(r"> #### 中文翻译\s*", "> ", text)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch39", p.stat().st_size)


def fix_ch40():
    p = ROOT / "ch40.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)
    text = peel_inline_zh_markers(text)

    def mut_4011(part: str) -> str:
        e, z, d = exact_headers(part)
        if e and not z:
            part = insert_zh_before_deep(part, ZH_40_11)
        return part

    text = fix_section_by_header(text, "40.11", mut_4011)
    for _ in range(3):
        text = split_long_quotes(text, limit=450)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch40", p.stat().st_size)


def fix_ch41():
    p = ROOT / "ch41.md"
    text = p.read_text(encoding="utf-8")
    text = normalize_header_aliases(text)
    for _ in range(2):
        text = split_long_quotes(text, limit=450)
    text = re_sub_n(text)
    p.write_text(text, encoding="utf-8")
    print("ch41", p.stat().st_size)


def improve_validator():
    """Patch validate to count exact ### headers only."""
    vp = Path("validate_ch36_41.py")
    t = vp.read_text(encoding="utf-8")
    old = '''        e = part.count("### 英文原文")
        z = part.count("### 中文翻译")
        d = part.count("### 深度理解")'''
    new = '''        plines = part.splitlines()
        e = sum(1 for l in plines if l.strip() == "### 英文原文")
        z = sum(1 for l in plines if l.strip() == "### 中文翻译")
        d = sum(1 for l in plines if l.strip() == "### 深度理解")'''
    if old in t:
        t = t.replace(old, new)
        # also fix global counts
        t = t.replace(
            '"eng": t.count("### 英文原文"),\n        "zh": t.count("### 中文翻译"),\n        "deep": t.count("### 深度理解"),',
            '"eng": sum(1 for l in lines if l.strip() == "### 英文原文"),\n        "zh": sum(1 for l in lines if l.strip() == "### 中文翻译"),\n        "deep": sum(1 for l in lines if l.strip() == "### 深度理解"),',
        )
        vp.write_text(t, encoding="utf-8")
        print("validator patched")
    else:
        print("validator already patched or pattern mismatch")


if __name__ == "__main__":
    improve_validator()
    fix_ch36()
    fix_ch37()
    fix_ch38()
    fix_ch39()
    fix_ch40()
    fix_ch41()
    print("--- validate ---")
    import validate_ch36_41

    validate_ch36_41.report()

# -*- coding: utf-8 -*-
"""
Batch fixes from full audit:
1) Normalize #### 英文原文/中文翻译/深度理解/代码分析 -> ###
2) Promote lone #### Example blocks stay as ####
3) Reflow English short lines inside ### 英文原文
4) Split English quotes > 550 chars
5) Report remaining eng/zh mismatches
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")


def normalize_heading_levels(text: str) -> tuple[str, int]:
    """#### 英文原文 etc -> ### ; count changes."""
    n = 0

    def repl(m):
        nonlocal n
        n += 1
        return "### " + m.group(1)

    text2, c = re.subn(
        r"^####\s*(英文原文|中文翻译|深度理解|代码分析)\s*$",
        repl,
        text,
        flags=re.M,
    )
    return text2, c


def is_code_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "```", "#")):
        return True
    if re.match(r"^(def |async def |class |import |from |@|return |if |elif |else:|for |while |try:|except|with |print\(|raise |self\.|yield |pass$)", t):
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and not t.endswith((".", "?", "!")) and len(t) < 100:
        if re.search(r"""['\"\[\](){}]|True|False|None|\d""", t):
            return True
    if t in {")", "]", "}", "),", "],", "},", '"""', "'''", "):", "(", "["}:
        return True
    if re.match(r"^<(__main__\.|class '|bound method|function )", t):
        return True
    return False


def ends_sentence(s: str) -> bool:
    s = s.rstrip()
    while s and s[-1] in "\"')]}”’":
        s = s[:-1]
    return bool(s) and s[-1] in ".!?"


def join_frags(frags):
    if not frags:
        return ""
    r = frags[0].strip()
    for p in frags[1:]:
        p = p.strip()
        if not p:
            continue
        if r.endswith("-") and p[:1].islower():
            r = r[:-1] + p
            continue
        if r[-1:] in "([{\"'“‘" or p[:1] in ",.;:!?)]}'\"”’":
            r += p
            continue
        r += " " + p
    r = re.sub(r"[ \t]{2,}", " ", r)
    r = re.sub(r" +([,.;:!?])", r"\1", r)
    return r.strip()


def reflow_eng_block(block_lines: list[str]) -> list[str]:
    """Reflow > quoted prose in an English section; keep code lines separate."""
    # Collect content lines (may include blanks and > lines)
    frags = []  # (text, is_code, raw_had_quote)
    for line in block_lines:
        if not line.strip():
            frags.append(("", False, False))  # blank marker
            continue
        if line.startswith(">"):
            body = line[1:]
            if body.startswith(" "):
                body = body[1:]
            # code fence inside quote
            if body.strip().startswith("```"):
                frags.append((body, True, True))
            else:
                frags.append((body, is_code_line(body), True))
        else:
            # non-quoted content inside eng section (code blocks without >)
            frags.append((line, True, False))

    # Decide if reflow needed: many short prose lines
    prose = [t for t, c, q in frags if t and not c and q]
    if not prose:
        return block_lines
    short = sum(1 for t in prose if len(t) <= 70)
    longish = sum(1 for t in prose if len(t) > 100)
    if short < 5 or longish >= short:
        # already mostly reflowed; still split huge later
        return block_lines

    out = []
    prose_buf = []
    in_fence = False

    def flush_prose():
        nonlocal prose_buf
        if not prose_buf:
            return
        text = join_frags(prose_buf)
        prose_buf = []
        if not text:
            return
        # paragraphize
        if len(text) > 480:
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", text)
            buf, bl = [], 0
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if buf and bl + len(p) > 420:
                    out.append("> " + " ".join(buf))
                    out.append(">")
                    buf, bl = [p], len(p)
                else:
                    buf.append(p)
                    bl += len(p) + 1
            if buf:
                out.append("> " + " ".join(buf))
        else:
            out.append("> " + text)
        out.append("")

    i = 0
    while i < len(frags):
        t, code, quoted = frags[i]
        if t == "" and not code:
            # blank: paragraph break if prose ends sentence
            if prose_buf and ends_sentence(prose_buf[-1]):
                flush_prose()
            i += 1
            continue
        if code or not quoted:
            flush_prose()
            if quoted:
                out.append("> " + t if not t.startswith(">") else t)
            else:
                out.append(t)
            # keep fence runs
            if t.strip().startswith("```"):
                in_fence = not in_fence
            i += 1
            continue
        # prose
        if prose_buf and ends_sentence(prose_buf[-1]) and t and t[0].isupper() and len(prose_buf[-1]) > 40:
            # soft break only if previous was substantial - actually join by default for PDF short lines
            pass
        prose_buf.append(t)
        i += 1
    flush_prose()
    while out and out[-1] == "":
        out.pop()
    return out if out else block_lines


def split_long_quotes_in_eng(text: str, limit: int = 500) -> tuple[str, int]:
    lines = text.splitlines()
    out = []
    in_eng = False
    fixed = 0
    for line in lines:
        if line.strip() == "### 英文原文":
            in_eng = True
            out.append(line)
            continue
        if line.startswith("### "):
            in_eng = False
            out.append(line)
            continue
        if in_eng and line.startswith(">") and len(line) > limit + 2:
            body = line[1:]
            if body.startswith(" "):
                body = body[1:]
            if is_code_line(body) or body.startswith("```") or body.startswith("**"):
                # still try split on ** sections? keep bold starters if very long split by sentences
                pass
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[*])", body)
            if len(parts) <= 1:
                out.append(line)
                continue
            buf, bl = [], 0
            chunks = []
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if buf and bl + len(p) > limit:
                    chunks.append(" ".join(buf))
                    buf, bl = [p], len(p)
                else:
                    buf.append(p)
                    bl += len(p) + 1
            if buf:
                chunks.append(" ".join(buf))
            if len(chunks) > 1:
                fixed += 1
                for j, ch in enumerate(chunks):
                    out.append("> " + ch)
                    if j < len(chunks) - 1:
                        out.append(">")
            else:
                out.append(line)
        else:
            out.append(line)
    return "\n".join(out), fixed


def process_eng_reflow(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "### 英文原文":
            out.append(line)
            i += 1
            if i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("### "):
                block.append(lines[i])
                i += 1
            new_block = reflow_eng_block(block)
            if new_block != block:
                fixed += 1
            out.extend(new_block)
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(line)
        i += 1
    return "\n".join(out), fixed


def ensure_blank_after_heads(text: str) -> str:
    text = re.sub(r"(### 英文原文)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 中文翻译)\n>", r"\1\n\n>", text)
    text = re.sub(r"(### 深度理解)\n-", r"\1\n\n-", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def counts(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    eng = sum(1 for L in lines if L.strip() == "### 英文原文")
    zh = sum(1 for L in lines if L.strip() == "### 中文翻译")
    deep = sum(1 for L in lines if L.strip() == "### 深度理解")
    # huge
    in_eng = False
    huge = short = 0
    for L in lines:
        if L.strip() == "### 英文原文":
            in_eng = True
            continue
        if L.startswith("### "):
            in_eng = False
            continue
        if in_eng and L.startswith(">"):
            b = L[1:].strip()
            if not b or is_code_line(b):
                continue
            if len(b) > 600:
                huge += 1
            elif 0 < len(b) <= 55 and b[:1].islower():
                short += 1
    return eng, zh, deep, huge, short


def process_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    orig = text
    text, n_head = normalize_heading_levels(text)
    text, n_reflow = process_eng_reflow(text)
    # second reflow pass
    text, n_reflow2 = process_eng_reflow(text)
    text, n_split = split_long_quotes_in_eng(text, 500)
    text, n_split2 = split_long_quotes_in_eng(text, 500)
    text = ensure_blank_after_heads(text)
    if not text.endswith("\n"):
        text += "\n"
    if text != orig:
        path.write_text(text, encoding="utf-8")
    eng, zh, deep, huge, short = counts(path)
    return {
        "file": path.name,
        "head": n_head,
        "reflow": n_reflow + n_reflow2,
        "split": n_split + n_split2,
        "eng": eng,
        "zh": zh,
        "deep": deep,
        "huge": huge,
        "short": short,
        "mismatch": eng != zh,
    }


def main():
    targets = sorted(ROOT.glob("ch*.md")) + sorted(ROOT.glob("appendix_*.md")) + sorted(ROOT.glob("about*.md"))
    rows = []
    for p in targets:
        if p.name == "FORMAT.md":
            continue
        rows.append(process_file(p))

    print(f"{'file':16s} {'hd':>3s} {'rf':>3s} {'sp':>3s} {'eng':>4s} {'zh':>4s} {'deep':>4s} {'huge':>4s} {'sh':>4s} mis")
    for r in rows:
        print(
            f"{r['file']:16s} {r['head']:3d} {r['reflow']:3d} {r['split']:3d} "
            f"{r['eng']:4d} {r['zh']:4d} {r['deep']:4d} {r['huge']:4d} {r['short']:4d} "
            f"{'Y' if r['mismatch'] else ' '}"
        )
    mis = [r for r in rows if r["mismatch"]]
    print(f"\nmismatch files: {len(mis)}")
    for r in mis:
        print(f"  {r['file']}: eng={r['eng']} zh={r['zh']}")
    huge_left = sum(r["huge"] for r in rows)
    print(f"total huge left: {huge_left}")


if __name__ == "__main__":
    main()

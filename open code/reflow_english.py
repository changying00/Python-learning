# -*- coding: utf-8 -*-
"""
Aggressive reflow: blank lines are IGNORED for prose joining.
Paragraph break only when previous ends with .!? and next starts uppercase,
or when entering a code/REPL run.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def unquote(line: str) -> str:
    if line.startswith("> "):
        return line[2:]
    if line.startswith(">"):
        return line[1:]
    return line


def is_code_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...", "$ ", "```")):
        return True
    if t.startswith(("<!", "<html", "<head", "<body", "<meta", "<link",
                      "<style", "<title", "<table", "<td", "<div", "</", "<p>", "<i>", "<a ")):
        return True
    # Real code headers only — not prose like "from which" / "class creation"
    if re.match(r"^(def|async def)\s+\w+\s*\(", t):
        return True
    if re.match(r"^class\s+[A-Z_]\w*\s*[\(:]", t):
        return True
    if re.match(r"^import\s+\w+", t):
        return True
    if re.match(r"^from\s+\w+(\.\w+)*\s+import\b", t):
        return True
    if re.match(r"^@\w+", t):
        return True
    # indented residual (2+ spaces or tab) that looks like code body
    if (s.startswith("  ") or s.startswith("\t")) and (
        re.match(r"^\s+(def |class |return |if |elif |else:|for |while |try:|except|with |print\(|self\.|cls\.)", s)
        or re.match(r"^\s+[A-Za-z_][\w.]*\s*=", s)
        or re.match(r"^\s+#", s)
    ):
        return True
    # short assignment code
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and not t.endswith((".", "?", "!")) and len(t) < 100:
        if re.search(r"""['\"\[\](){}]|True|False|None|\d""", t):
            return True
    # lone brace / triple quote
    if t in {")", "]", "}", "),", "],", "},", '"""', "'''", "):", "(", "["}:
        return True
    return False


def ends_sentence(s: str) -> bool:
    s = s.rstrip()
    while s and s[-1] in "\"')]}”’":
        s = s[:-1]
    return bool(s) and s[-1] in ".!?"


def starts_cap(s: str) -> bool:
    s = s.lstrip()
    return bool(s) and (s[0].isupper() or s[0] in "\"'“‘0123456789*")


def join_frags(frags):
    if not frags:
        return ""
    result = frags[0].strip()
    for p in frags[1:]:
        p = p.strip()
        if not p:
            continue
        if result.endswith("-") and p[:1].islower():
            result += p
            continue
        if result[-1:] in "([{\"'“‘" or p[:1] in ",.;:!?)]}'\"”’":
            result += p
            continue
        result += " " + p
    result = re.sub(r"[ \t]{2,}", " ", result)
    result = re.sub(r" +([,.;:!?])", r"\1", result)
    result = re.sub(r"\( ", "(", result)
    result = re.sub(r" \)", ")", result)
    return result.strip()


def reflow_block(block_lines):
    frags = []
    for line in block_lines:
        raw = unquote(line)
        if not raw.strip():
            continue  # ignore blanks entirely
        frags.append((raw.rstrip(), is_code_line(raw)))

    if not frags:
        return block_lines

    # already good?
    prose_only = [t for t, c in frags if not c]
    if prose_only:
        longish = sum(1 for t in prose_only if len(t) > 120)
        shortish = sum(1 for t in prose_only if len(t) <= 80)
        if longish >= 3 and shortish <= max(2, longish // 3):
            return block_lines

    out = []
    prose = []

    def flush():
        nonlocal prose
        if prose:
            text = join_frags(prose)
            if text:
                out.append(f"> {text}")
                out.append(">")
            prose = []

    i = 0
    while i < len(frags):
        s, code = frags[i]
        if code:
            flush()
            while i < len(frags) and frags[i][1]:
                out.append(f"> {frags[i][0]}")
                i += 1
            out.append(">")
            continue

        # paragraph break before this frag?
        if prose and ends_sentence(prose[-1]) and starts_cap(s):
            # avoid breaking on abbreviations like "e.g." "i.e." "etc." mid flow —
            # if last frag is very short (< 40) and doesn't look like full sentence end of paragraph, still break is OK for book style
            flush()
        prose.append(s.strip())
        i += 1
    flush()
    while out and out[-1] == ">":
        out.pop()
    return out if out else block_lines


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    out = []
    i = 0
    fixed = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "### 英文原文":
            out.append(line)
            i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("### "):
                block.append(lines[i])
                i += 1
            new_block = reflow_block(block)
            if new_block != block:
                fixed += 1
            out.append("")
            out.extend(new_block)
            out.append("")
            continue
        out.append(line)
        i += 1

    new_text = "\n".join(out)
    new_text = re.sub(r"^# 第(\d+)章", r"# 第 \1 章", new_text, count=1, flags=re.M)
    new_text = re.sub(r"(> \*\*本章地位\*\*[^\n]*)\n+---", r"\1\n\n---", new_text, count=1)
    new_text = re.sub(r"\n{3,}", "\n\n", new_text)
    if not new_text.endswith("\n"):
        new_text += "\n"
    path.write_text(new_text, encoding="utf-8")
    return fixed


def stats(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    in_eng = False
    long_q = short_q = 0
    for line in lines:
        if line.startswith("### 英文原文"):
            in_eng = True
            continue
        if line.startswith("### "):
            in_eng = False
            continue
        if in_eng and line.startswith(">"):
            body = line[1:].strip()
            if len(body) > 100:
                long_q += 1
            elif body:
                short_q += 1
    return long_q, short_q


def main():
    targets = sys.argv[1:] or ["ch38.md", "ch40.md", "ch41.md"]
    for name in targets:
        p = Path("chapters") / name
        n = process_file(p)
        # second pass
        n2 = process_file(p)
        long_q, short_q = stats(p)
        print(f"{name}: fixed={n}/{n2} long={long_q} short={short_q}")
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if line.strip() == "### 英文原文":
                print("  sample:")
                for j in range(i, min(i + 16, len(lines))):
                    print("   ", lines[j][:160])
                break
        print()


if __name__ == "__main__":
    main()

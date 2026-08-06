# -*- coding: utf-8 -*-
"""Second polish: fix residual code glued to prose in English sections."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CHAP = Path(__file__).resolve().parent / "chapters"


CODE_START = re.compile(
    r"(?P<code>"
    r"(?:^|\s)(?:"
    r"person\.\w+.*"  # will use differently
    r"))"
)


def split_glued(text: str) -> list[tuple[str, str]]:
    """Split prose that has code statements glued before continuing prose."""
    s = text.strip()
    if not s:
        return []

    # Case: starts with code call/assign then prose capital
    # e.g. "person.getName() person.setName('value') The problem with..."
    m = re.match(
        r"^((?:[A-Za-z_][\w.]*\s*(?:=|\(|\.)[^\.!?]*?(?:\)|'[^']*'|\"[^\"]*\")\s*)+)([A-Z].*)$",
        s,
    )
    if m and len(m.group(1)) < 200:
        code = m.group(1).strip()
        rest = m.group(2).strip()
        # break code into lines on patterns
        code = re.sub(r"\s+(?=[A-Za-z_][\w.]*\s*(?:=|\())", "\n", code)
        code = re.sub(r"\s+#\s*", "\n# ", code)
        segs = [("code", code)]
        segs.extend(split_glued(rest) or [("prose", rest)])
        return segs

    # Case: prose ends with colon then code then more prose
    # "basic attribute syntax: person.name # Fetch ... In most cases,..."
    m = re.search(r"^(.*?:\s*)([a-z_][\w.]*\s*(?:=|\.|#).+)$", s)
    if m:
        head = m.group(1).strip()
        tail = m.group(2).strip()
        # find prose resume: "In most" "The " "This " etc after code
        m2 = re.search(
            r"(?<=\s)(?=(?:In |The |This |That |These |Those |If |When |While |Although |Because |Since |Moreover |However |Still |For |As |To |We |You |It ))",
            tail,
        )
        if m2 and m2.start() > 5:
            code = tail[: m2.start()].strip()
            rest = tail[m2.start():].strip()
            code = re.sub(r"\s+#\s*", "\n# ", code)
            code = re.sub(r"\s+(?=[a-z_][\w.]*\s*=)", "\n", code)
            segs = []
            if head:
                segs.append(("prose", head))
            segs.append(("code", code))
            segs.extend(split_glued(rest) or [("prose", rest)])
            return segs

    # Case: "# comment text more code" fragments that are mostly code
    if s.startswith("#") and len(s) < 120:
        return [("code", s)]

    # Case: line is mostly short code statements
    if is_mostly_code(s):
        c = re.sub(r"\s+#\s*", "\n# ", s)
        c = re.sub(r"\s+(?=[A-Za-z_][\w.]*\s*(?:=|\())", "\n", c)
        return [("code", c)]

    return [("prose", s)]


def is_mostly_code(s: str) -> bool:
    if len(s) > 180:
        return False
    if re.match(r"^(def |class |import |from |return |self\.|cls\.|>>>|@)", s):
        return True
    # high density of code tokens, low prose words
    prose_words = len(re.findall(r"\b(the|and|that|which|with|from|this|are|is|for|can|will|should)\b", s, re.I))
    code_marks = len(re.findall(r"[=()\[\]{}]|->|::", s))
    if code_marks >= 2 and prose_words <= 1 and not s.endswith((".", "?", "!")):
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", s) and not s.endswith((".", "?", "!")):
        return True
    return False


def split_long_prose(s: str, limit: int = 320) -> list[str]:
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) <= limit:
        return [s] if s else []
    parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[]|__)", s)
    out, buf, n = [], [], 0
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if buf and n + len(p) > limit:
            out.append(" ".join(buf))
            buf, n = [p], len(p)
        else:
            buf.append(p)
            n += len(p) + 1
    if buf:
        out.append(" ".join(buf))
    return out or [s]


def polish_section(block_lines: list[str]) -> list[str]:
    # parse to blocks
    blocks: list[tuple[str, str]] = []
    i = 0
    while i < len(block_lines):
        line = block_lines[i]
        if not line.startswith(">"):
            i += 1
            continue
        body = line[1:]
        if body.startswith(" "):
            body = body[1:]
        if body.strip() == "```python":
            code = []
            i += 1
            while i < len(block_lines):
                ln = block_lines[i]
                b = ln[1:] if ln.startswith(">") else ln
                if b.startswith(" "):
                    b = b[1:]
                if b.strip() == "```":
                    i += 1
                    break
                code.append(b)
                i += 1
            blocks.append(("code", "\n".join(code)))
            continue
        if body.strip() and body.strip() != "```":
            blocks.append(("prose", body.strip()))
        i += 1

    newb: list[tuple[str, str]] = []
    for kind, text in blocks:
        if kind == "code":
            # fix lone "person.name #" crumbs — merge later
            if text.strip():
                newb.append(("code", text))
            continue
        for sk, st in split_glued(text):
            if sk == "prose":
                for chunk in split_long_prose(st):
                    newb.append(("prose", chunk))
            else:
                newb.append(("code", st))

    # merge adjacent code; drop trivial code that's just "#"
    merged: list[tuple[str, str]] = []
    for kind, text in newb:
        if kind == "code":
            t = text.strip()
            if t in {"#", "```", ""}:
                continue
            # expand "person.name #" style
            if t.endswith("#") and len(t) < 40:
                t = t  # keep, maybe next prose has comment words — leave
            if merged and merged[-1][0] == "code":
                merged[-1] = ("code", merged[-1][1] + "\n" + t)
            else:
                merged.append(("code", t))
        else:
            merged.append(("prose", text))

    # fix: code block that is only "person.name #" followed by prose starting with "Fetch attribute"
    fixed: list[tuple[str, str]] = []
    i = 0
    while i < len(merged):
        kind, text = merged[i]
        if (
            kind == "code"
            and i + 1 < len(merged)
            and merged[i + 1][0] == "prose"
            and text.rstrip().endswith("#")
        ):
            # pull comment words from start of next prose if they look like comment
            nxt = merged[i + 1][1]
            m = re.match(r"^((?:Fetch|Change|Make|Run|Add|Client|Normal|Class|Too|See|Or|And)[^A-Z]*)\s+([A-Z].*)$", nxt)
            # simpler: if next starts with capital verb phrase before another code
            words = nxt.split()
            # if pattern "Fetch attribute value person.name = ..."
            m = re.match(
                r"^((?:Fetch|Change|Make|Run|Add|Normal|Clients|Class)[^.]*?)((?:[a-z_][\w.]*\s*=|[A-Z].*))$",
                nxt,
            )
            if m and "attribute" in m.group(1).lower():
                comment = m.group(1).strip()
                rest = m.group(2).strip()
                fixed.append(("code", text.rstrip() + " " + comment))
                for sk, st in split_glued(rest) or [("prose", rest)]:
                    fixed.append((sk, st))
                i += 2
                continue
            # generic: attach first 2-5 words as comment if code ends with #
            m = re.match(r"^((?:\S+\s+){1,5}\S+)\s+(.*)$", nxt)
            if m and not m.group(1).endswith((".", "?", "!")):
                # only if first words are lowercase-ish comment style
                first = m.group(1)
                if first[0].isupper() and len(first) < 40 and " the " not in (" " + first.lower() + " "):
                    fixed.append(("code", text.rstrip() + " " + first))
                    rest = m.group(2).strip()
                    for sk, st in split_glued(rest) or [("prose", rest)]:
                        if sk == "prose":
                            for chunk in split_long_prose(st):
                                fixed.append(("prose", chunk))
                        else:
                            fixed.append((sk, st))
                    i += 2
                    continue
        fixed.append((kind, text))
        i += 1

    # emit
    out: list[str] = []
    for kind, text in fixed:
        if kind == "code":
            out.append(">")
            out.append("> ```python")
            for cl in text.splitlines():
                out.append(f"> {cl}")
            out.append("> ```")
            out.append(">")
        else:
            t = text.strip()
            if t:
                out.append(f"> {t}")
                out.append(">")
    while out and out[-1] == ">":
        out.pop()
    return out


def process(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    i = 0
    nfix = 0
    while i < len(lines):
        if lines[i].strip() == "### 英文原文":
            out.append(lines[i])
            i += 1
            if i < len(lines) and lines[i].strip() == "":
                out.append(lines[i])
                i += 1
            block = []
            while i < len(lines) and not lines[i].startswith("### "):
                block.append(lines[i])
                i += 1
            newb = polish_section(block)
            if newb != block:
                nfix += 1
            out.extend(newb)
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")

    huge = long = short = 0
    in_eng = in_code = False
    for line in text.splitlines():
        if line.strip() == "### 英文原文":
            in_eng = True
            in_code = False
            continue
        if line.startswith("### "):
            in_eng = False
            continue
        if not in_eng or not line.startswith(">"):
            continue
        body = line[1:].strip()
        if body.startswith("```"):
            in_code = body.startswith("```python")
            if body == "```":
                in_code = False
            continue
        if in_code or not body:
            continue
        if len(body) > 400:
            huge += 1
        if len(body) > 100:
            long += 1
        elif len(body) < 40:
            short += 1
    print(f"{path.name}: polished={nfix} long={long} short={short} huge={huge}")


def main():
    for n in (38, 40):
        process(CHAP / f"ch{n:02d}.md")
    lines = (CHAP / "ch38.md").read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if "Why Manage Attributes" in line:
            for j in range(i, min(i + 50, len(lines))):
                print(f"{j+1:4d}|{lines[j][:120]}")
            break


if __name__ == "__main__":
    main()

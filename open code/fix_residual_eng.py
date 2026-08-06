# -*- coding: utf-8 -*-
"""Fix residual English glue issues in ch38/ch40."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CHAP = Path(__file__).resolve().parent / "chapters"


def fix_text(text: str) -> str:
    # 1) classic person.name snippet
    text = text.replace(
        "> ```python\n"
        "> person.name #\n"
        "> ```\n"
        ">\n"
        "> Fetch attribute value person.name = value # Change attribute value "
        "In most cases, the attribute lives in the object itself or is inherited "
        "from a class from which it derives.",
        "> ```python\n"
        "> person.name                 # Fetch attribute value\n"
        "> person.name = value         # Change attribute value\n"
        "> ```\n"
        ">\n"
        "> In most cases, the attribute lives in the object itself or is inherited "
        "from a class from which it derives.",
    )

    # 2) ch40 bullet list glued then wrongly fenced
    text = text.replace(
        "> Just like decorators, though, metaclasses: Provide a more uniform and explicit structure "
        "Help ensure that application programmers won’t forget to augment their classes according to an API’s requirements "
        "Avoid code redundancy and its associated maintenance costs by factoring class customization logic into a single location "
        "To illustrate, suppose we want to automatically insert a method into a set of classes.",
        "> Just like decorators, though, metaclasses:\n"
        ">\n"
        "> - Provide a more uniform and explicit structure\n"
        "> - Help ensure that application programmers won’t forget to augment their classes according to an API’s requirements\n"
        "> - Avoid code redundancy and its associated maintenance costs by factoring class customization logic into a single location\n"
        ">\n"
        "> To illustrate, suppose we want to automatically insert a method into a set of classes.",
    )
    # if already split across fence wrongly:
    text = re.sub(
        r"> Just like decorators, though, metaclasses: Provide a more uniform and explicit structure Help ensure that application programmers won’t forget to augment their classes according to an API’s requirements Avoid code redundancy and its associated maintenance costs by\n>\n>\n> ```python\n> class customization logic into a single location To illustrate, suppose we want to automatically insert a method into a set of c\n> ```\n>",
        "> Just like decorators, though, metaclasses:\n"
        ">\n"
        "> - Provide a more uniform and explicit structure\n"
        "> - Help ensure that application programmers won’t forget to augment their classes according to an API’s requirements\n"
        "> - Avoid code redundancy and its associated maintenance costs by factoring class customization logic into a single location\n"
        ">\n"
        "> To illustrate, suppose we want to automatically insert a method into a set of classes.\n>",
        text,
    )

    # 3) comment lines outside fence that continue into prose
    # "> # Make an instance X.extra() # Run the extra methods Sometimes, though,"
    def fix_hash_prose(m: re.Match) -> str:
        body = m.group(1)
        # split at first clearly prose capital after codey hash comments
        mm = re.match(
            r"^(#.*?)((?:Sometimes|Although|Because|When|If |The |This |That |In |However|Moreover|Still|Of course|We |You |To ).*)$",
            body,
        )
        if not mm:
            return m.group(0)
        codeish, prose = mm.group(1).strip(), mm.group(2).strip()
        # turn multiple # comments / calls into code block
        codeish = re.sub(r"\s+#\s*", "\n# ", codeish)
        codeish = re.sub(r"\s+(?=[A-Za-z_][\w.]*\()", "\n", codeish)
        lines = [" >", " > ```python"]
        # fix leading space pattern - use proper
        out_lines = [">", "> ```python"]
        for cl in codeish.split("\n"):
            if cl.strip():
                out_lines.append("> " + cl.strip())
        out_lines.append("> ```")
        out_lines.append(">")
        out_lines.append("> " + prose)
        return "\n".join(out_lines)

    text = re.sub(
        r"^> (# .*(?:Sometimes|Although|Because|When|If |The |This |That |In |However|Moreover|Still|Of course|We |You |To ).*)$",
        fix_hash_prose,
        text,
        flags=re.M,
    )

    # 4) Remove absurd code fences that are pure prose starting with "class customization" or long English without =
    def strip_bad_fences(text: str) -> str:
        lines = text.splitlines()
        out = []
        i = 0
        while i < len(lines):
            if lines[i].strip() == "> ```python":
                # gather
                j = i + 1
                body = []
                while j < len(lines) and lines[j].strip() != "> ```":
                    b = lines[j][1:] if lines[j].startswith(">") else lines[j]
                    if b.startswith(" "):
                        b = b[1:]
                    body.append(b)
                    j += 1
                block = "\n".join(body).strip()
                # bad if long prose, no def/class real, starts with lowercase words of prose
                is_bad = False
                if re.match(r"^class customization logic", block):
                    is_bad = True
                if (
                    len(block) > 80
                    and not re.search(r"\b(def |class [A-Z]|import |from |return |self\.|>>> )", block)
                    and len(re.findall(r"\b(the|and|that|with|from|this|into|suppose|want)\b", block, re.I)) >= 3
                ):
                    is_bad = True
                if is_bad:
                    # emit as prose paragraphs
                    for chunk in re.split(r"(?<=[.!?]) +", block):
                        if chunk.strip():
                            out.append("> " + chunk.strip())
                            out.append(">")
                    if out and out[-1] == ">":
                        out.pop()
                    i = j + 1 if j < len(lines) and lines[j].strip() == "> ```" else j
                    continue
                # keep fence
                out.append(lines[i])
                out.extend(lines[i + 1 : j + 1] if j < len(lines) else lines[i + 1 : j])
                i = j + 1 if j < len(lines) else j
                continue
            out.append(lines[i])
            i += 1
        return "\n".join(out)

    text = strip_bad_fences(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


def main():
    for n in (38, 40):
        p = CHAP / f"ch{n:02d}.md"
        old = p.read_text(encoding="utf-8")
        new = fix_text(old)
        p.write_text(new, encoding="utf-8")
        print(f"{p.name}: changed={old != new} len={len(new)}")

    # samples
    for n, key in ((38, "Why Manage Attributes"), (40, "Downside of")):
        lines = (CHAP / f"ch{n:02d}.md").read_text(encoding="utf-8").splitlines()
        for i, l in enumerate(lines):
            if key in l:
                print(f"==== ch{n} {key} ====")
                for j in range(i, min(i + 35, len(lines))):
                    print(f"{j+1:4d}|{lines[j][:120]}")
                break


if __name__ == "__main__":
    main()

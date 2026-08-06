# -*- coding: utf-8 -*-
"""Simple aggressive reflow of PDF chapter extracts."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEADINGS = {
    38: [
        "Why Manage Attributes?",
        "Inserting Code to Run on Attribute Access",
        "Properties",
        "The Basics",
        "A First Example",
        "Computed Attributes",
        "Coding Properties with Decorators",
        "Setter and deleter decorators",
        "Descriptors",
        "Descriptor method arguments",
        "Read-only descriptors",
        "Using State Information in Descriptors",
        "How Properties and Descriptors Relate",
        "Descriptors and slots and more",
        "__getattr__ and __getattribute__",
        "Avoiding loops in attribute interception methods",
        "Using __getattribute__",
        "__getattr__ and __getattribute__ Compared",
        "Management Techniques Compared",
        "Intercepting Built-in Operation Attributes",
        "Revisiting Chapter 28's delegation example",
        "Revisiting Chapter 28’s delegation example",
        "Example: Attribute Validations",
        "Using Properties to Validate",
        "Testing code",
        "Using Descriptors to Validate",
        "Using __getattr__ to Validate",
        "Using __getattribute__ to Validate",
        "Chapter Summary",
        "Test Your Knowledge: Quiz",
        "Test Your Knowledge: Answers",
        "NOTE",
    ],
    40: [
        "To Metaclass or Not to Metaclass",
        "The Downside of “Helper” Functions",
        'The Downside of "Helper" Functions',
        "Metaclasses Versus Class Decorators: Round 1",
        "The Metaclass Model",
        "Classes Are Instances of type",
        "Metaclasses Are Subclasses of type",
        "Class Statements Call a type",
        "Class Statements Can Choose a type",
        "Metaclass Method Protocol",
        "Coding Metaclasses",
        "A Basic Metaclass",
        "Customizing Construction and Initialization",
        "Other Metaclass Coding Techniques",
        "Using simple factory functions",
        "Overloading class creation calls with normal classes",
        "Managing Classes with Metaclasses and Decorators",
        "Adding methods to classes",
        "Automatically decorating class methods",
        "Inheritance: The Finale",
        "Metaclass Versus Superclass",
        "Metaclass Inheritance",
        "Python Inheritance Algorithm: The Simple Version",
        "The descriptors deviation",
        "The Descriptors Deviation",
        "Python Inheritance Algorithm: The Less Simple Version",
        "The assignment addendum",
        "The Assignment Addendum",
        "The super supplement",
        "The Super Supplement",
        "The built-ins bifurcation",
        "The Built-ins Bifurcation",
        "The Inheritance Wrap-Up",
        "Metaclass Methods",
        "Metaclass Methods Versus Class Methods",
        "Operator Overloading in Metaclass Methods",
        "Metaclass Methods Versus Instance Methods",
        "Chapter Summary",
        "Test Your Knowledge: Quiz",
        "Test Your Knowledge: Answers",
        "NOTE",
    ],
}


def is_code(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if t.startswith((">>>", "...")):
        return True
    if t == "$" or t.startswith("$ "):
        return True
    if re.match(r"^(def|async def)\s+\w+\s*\(", t):
        return True
    if re.match(r"^class\s+[A-Z_]\w*(\s*[\(:]|\s*$)", t):
        return True
    if re.match(r"^from\s+[A-Za-z_]\w*(\.\w+)*\s+import\b", t):
        return True
    if re.match(r"^import\s+[A-Za-z_]\w*", t):
        return True
    if re.match(r"^@[A-Za-z_]", t):
        return True
    if re.match(r"^(return|raise|yield|pass)\b", t) and not t.endswith("."):
        return True
    if re.match(r"^print\s*\(", t):
        return True
    if re.match(r"^self\.\w+", t):
        return True
    if t in ("else:", "try:", "finally:", "pass", "...", "…"):
        return True
    # if/for/while/with only when ends with :
    if re.match(r"^(if|elif|else|for|while|with|try|except|finally)\b", t) and t.rstrip().endswith(":"):
        return True
    if re.match(r"^[A-Za-z_][\w.]*\s*=\s*\S", t) and len(t) < 90 and not t.endswith((".", "?", "!")):
        if re.search(r"""['\"\[\](){}]|True|False|None|\d|lambda|__\w+__""", t):
            return True
    if t in {")", "]", "}", "),", "],", "},", '"""', "'''", "):", "(", "["}:
        return True
    if re.match(r"^(File \"|Traceback|TypeError:|AttributeError:|NameError:|ValueError:|SyntaxError:|KeyError:)", t):
        return True
    if re.match(r"^<(__main__\.|class '|bound method|function |slot wrapper)", t):
        return True
    return False


def is_repl_out(s: str) -> bool:
    t = s.strip()
    if not t:
        return False
    if re.match(r"^-{3,}$", t):
        return True
    if re.match(r"^-?\d+(\.\d+)?$", t):
        return True
    if t in ("None", "True", "False"):
        return True
    if re.match(r"^['\"].{0,70}['\"]$", t):
        return True
    if re.match(r"^<.*>$", t) and len(t) < 120:
        return True
    return False


def ends_sent(s: str) -> bool:
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
    r = re.sub(r"\( ", "(", r)
    r = re.sub(r" \)", ")", r)
    return r.strip()


def heading_of(s, heads):
    t = s.strip()
    if t in heads:
        return t
    if re.match(r"^Example\s+\d+-\d+", t):
        return t
    return None


def reflow(raw: str, chap: int) -> str:
    heads = set(HEADINGS[chap])
    lines = [re.sub(r"[ ]{2,}", " ", ln.replace("\t", " ")).rstrip() for ln in raw.splitlines()]
    n = len(lines)
    i = 0
    blocks = []

    # title
    while i < n and not lines[i].strip():
        i += 1
    if i < n and re.match(r"^Chapter\s+\d+\.", lines[i].strip()):
        chap_line = lines[i].strip()
        if not chap_line.endswith("."):
            chap_line += "."
        else:
            # "Chapter 38." already
            pass
        i += 1
        tw = []
        while i < n:
            t = lines[i].strip()
            if not t:
                i += 1
                if tw:
                    break
                continue
            if heading_of(t, heads) or is_code(t) or (len(t) > 50 and ends_sent(t)):
                break
            if len(t) <= 40 and t[0].isupper() and not ends_sent(t):
                tw.append(t)
                i += 1
                if t.endswith("and"):
                    continue
                if chap == 40 and "Inheritance" not in " ".join(tw):
                    continue
                break
            break
        blocks.append(("H", chap_line.rstrip(".") + ". " + " ".join(tw)))

    prose, code = [], []
    in_code = False

    def fp():
        nonlocal prose
        if not prose:
            return
        text = join_frags(prose)
        prose = []
        if not text:
            return
        if len(text) > 500:
            parts = re.split(r"(?<=[.!?]) +(?=[A-Z\"'(\[])", text)
            buf, bl = [], 0
            for p in parts:
                p = p.strip()
                if not p:
                    continue
                if buf and bl + len(p) > 430:
                    blocks.append(("P", " ".join(buf)))
                    buf, bl = [p], len(p)
                else:
                    buf.append(p)
                    bl += len(p) + 1
            if buf:
                blocks.append(("P", " ".join(buf)))
        else:
            blocks.append(("P", text))

    def fc():
        nonlocal code, in_code
        if code:
            while code and not code[0].strip():
                code.pop(0)
            while code and not code[-1].strip():
                code.pop()
            if code:
                blocks.append(("C", "\n".join(code)))
        code, in_code = [], False

    while i < n:
        t = lines[i].strip()
        i += 1
        if not t:
            if in_code:
                j = i
                while j < n and not lines[j].strip():
                    j += 1
                if j < n and (is_code(lines[j].strip()) or lines[j].strip().startswith((">>>", "...", "$")) or is_repl_out(lines[j].strip())):
                    code.append("")
                else:
                    fc()
            continue

        h = heading_of(t, heads)
        if h:
            fp()
            fc()
            blocks.append(("H", h))
            continue

        if is_code(t) or t.startswith((">>>", "...")) or t in ("$",) or t.startswith("$ "):
            fp()
            in_code = True
            code.append(t)
            continue

        if in_code:
            prev = code[-1] if code else ""
            keep = False
            if is_code(t) or is_repl_out(t) or t.startswith((">>>", "...", "$")):
                keep = True
            elif prev.startswith(("$", ">>>", "...")) or is_repl_out(prev):
                # short outputs like "Sue Jones"
                if len(t) < 60 and not (ends_sent(t) and " the " in f" {t.lower()} "):
                    keep = True
            elif re.match(r"^(if not |if |elif |else:|for |while |return |raise |self\.|print\(|def |class |@)", t) and (
                t.endswith(":") or "(" in t or t.startswith(("self.", "return", "raise", "def ", "class ", "@"))
            ):
                keep = True
            if keep:
                # but don't keep clear prose
                if ends_sent(t) and len(t) > 50 and t[0].isupper() and " the " in f" {t.lower()} ":
                    keep = False
            if keep:
                code.append(t)
                continue
            fc()

        if re.match(r"^\d+$", t):
            prose.append(t + ".")
            continue

        prose.append(t)
        if sum(len(x) for x in prose) > 420 and ends_sent(t):
            j = i
            while j < n and not lines[j].strip():
                j += 1
            if j < n:
                nxt = lines[j].strip()
                if (
                    nxt
                    and nxt[0].isupper()
                    and len(nxt) > 20
                    and not is_code(nxt)
                    and not heading_of(nxt, heads)
                    and not nxt.startswith((">>>", "...", "$"))
                ):
                    fp()

    fp()
    fc()

    out = []
    for k, c in blocks:
        if k == "H":
            out += [c, ""]
        elif k == "P":
            out += [c, ""]
        else:
            out += ["```python", c, "```", ""]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"
    return text


def main():
    import PyPDF2

    reader = PyPDF2.PdfReader("learning-python-powerful-6th.pdf")
    ranges = {38: (1499, 1556), 40: (1641, 1691)}
    for num, (a, b) in ranges.items():
        parts = []
        for p in range(a - 1, b):
            t = reader.pages[p].extract_text() or ""
            t = t.replace("\t", " ")
            parts.append("\n".join(re.sub(r"[ ]{2,}", " ", ln) for ln in t.split("\n")))
        raw = "\n".join(parts)
        cleaned = reflow(raw, num)
        Path(f"chapters/ch{num:02d}.txt").write_text(cleaned, encoding="utf-8")
        lines = cleaned.splitlines()
        orphan = sum(
            1
            for L in lines
            if L and L[0].islower() and len(L) < 70 and not L.startswith("```")
            and not re.match(r"^(def |class |import |from |return |self\.|if |for |print)", L)
        )
        print(f"ch{num:02d}: chars={len(cleaned)} lines={len(lines)} orphan_lower={orphan}")
        for L in lines[:40]:
            print(L[:130])
        print("====")


if __name__ == "__main__":
    main()

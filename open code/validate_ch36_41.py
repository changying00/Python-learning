# -*- coding: utf-8 -*-
"""Validate ch36-ch41 format against FORMAT.md / ch01 style."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("chapters")
QUIZ_WHITELIST = re.compile(
    r"(Quiz|Answers|测验|答案|技术拓展|学习建议|本章总结)", re.I
)


def analyze(n: int) -> dict:
    p = ROOT / f"ch{n:02d}.md"
    t = p.read_text(encoding="utf-8")
    lines = t.splitlines()
    h2s = [(i + 1, l) for i, l in enumerate(lines) if l.startswith("## ")]
    unnum = []
    for ln, h in h2s:
        if re.match(r"^## \d+\.\d+", h):
            continue
        if h.startswith("## 技术拓展") or h.startswith("## 学习建议"):
            continue
        if h.startswith("# ") and "本章总结" in h:
            continue
        unnum.append((ln, h[:90]))

    long_eng = []
    in_e = False
    for i, l in enumerate(lines):
        if l.startswith("### 英文原文"):
            in_e = True
            continue
        if l.startswith("### "):
            in_e = False
            continue
        if in_e and l.startswith(">") and len(l) > 500:
            body = l[1:].lstrip()
            # Scheme A residual: ignore code-glued long lines
            codeish = any(
                k in body
                for k in (">>>", " def ", " class ", " return ", "print(", "self.", "cls.")
            ) or body.lstrip().startswith((">>>", "def ", "class ", "# ", "if ", "for "))
            pure = body.count(". ") >= 2 and not codeish
            if pure:
                long_eng.append(i + 1)

    parts = re.split(r"(?m)^(?=## )", t)
    bad_pair = []
    for part in parts[1:]:
        first = part.splitlines()[0] if part.splitlines() else ""
        if first.startswith("## 技术") or first.startswith("## 学习"):
            continue
        plines = part.splitlines()
        e = sum(1 for l in plines if l.strip() == "### 英文原文")
        z = sum(1 for l in plines if l.strip() == "### 中文翻译")
        d = sum(1 for l in plines if l.strip() == "### 深度理解")
        if e == 0 and z == 0 and d == 0:
            continue
        flags = []
        # Scheme A: allow multiple eng/zh blocks inside one ## (subtopics),
        # only flag hard structural gaps.
        if e and not z:
            flags.append("no-zh")
        if e and not d and not QUIZ_WHITELIST.search(first):
            flags.append("no-deep")
        if z and not e:
            flags.append("zh-only")
        if d and not e and not QUIZ_WHITELIST.search(first):
            flags.append("deep-only")
        # soft note if counts differ a lot (not hard fail unless no-zh)
        if e and z and abs(e - z) >= 3:
            flags.append(f"e/z-skew={e}/{z}")
        if flags:
            bad_pair.append((first[:70], flags))

    return {
        "n": n,
        "size": p.stat().st_size,
        "title_ok": bool(re.match(rf"^# 第 {n} 章", lines[0] if lines else "")),
        "h2": len(h2s),
        "unnum": unnum,
        "eng": sum(1 for l in lines if l.strip() == "### 英文原文"),
        "zh": sum(1 for l in lines if l.strip() == "### 中文翻译"),
        "deep": sum(1 for l in lines if l.strip() == "### 深度理解"),
        "long_eng": long_eng,
        "summary": "本章总结" in t,
        "tech": "技术拓展" in t,
        "advice": "学习建议" in t,
        "bad_pair": bad_pair,
        "hr": t.count("\n---\n"),
    }


def report(ns=range(36, 42)):
    ok_all = True
    for n in ns:
        a = analyze(n)
        problems = []
        if not a["title_ok"]:
            problems.append("title")
        if a["unnum"]:
            problems.append(f"unnum={len(a['unnum'])}")
        if a["long_eng"]:
            problems.append(f"long={len(a['long_eng'])}")
        if a["bad_pair"]:
            problems.append(f"pair={len(a['bad_pair'])}")
        if not a["summary"]:
            problems.append("no-summary")
        if not a["tech"]:
            problems.append("no-tech")
        if not a["advice"]:
            problems.append("no-advice")
        status = "OK" if not problems else "ISSUE"
        if problems:
            ok_all = False
        print(
            f"ch{a['n']:02d} [{status}] size={a['size']} h2={a['h2']} "
            f"e/z/d={a['eng']}/{a['zh']}/{a['deep']} hr={a['hr']} "
            f"problems={problems or '-'}"
        )
        for ln, h in a["unnum"][:8]:
            print(f"    unnum L{ln}: {h}")
        if len(a["unnum"]) > 8:
            print(f"    ... +{len(a['unnum']) - 8} more unnum")
        for first, flags in a["bad_pair"][:6]:
            print(f"    pair {flags}: {first}")
        if len(a["bad_pair"]) > 6:
            print(f"    ... +{len(a['bad_pair']) - 6} more pair")
    return ok_all


if __name__ == "__main__":
    report()

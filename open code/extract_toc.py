# -*- coding: utf-8 -*-
"""Bookmark(ToC)-driven PDF text extraction.

Reads the PDF outline (bookmarks) to determine section start pages, then
extracts chapter/appendix text into independent .txt files. Replaces the old
hardcoded CHAPTER_STARTS / NUM_PAGES approach that glued Appendix+Index+
About the Author onto the last chapter.
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

try:
    import PyPDF2
except ImportError:
    sys.exit("PyPDF2 is required")

PDF = "learning-python-powerful-6th.pdf"
OUT_DIR = "chapters"


def clean(text):
    text = text.replace("\t", " ")
    lines = []
    for ln in text.split("\n"):
        ln = re.sub(r"[ ]{2,}", " ", ln)
        lines.append(ln)
    return "\n".join(lines)


def walk(items, depth=0, found=None):
    found = found if found is not None else []
    for it in items:
        if isinstance(it, list):
            walk(it, depth + 1, found)
        else:
            found.append(it)
    return found


def page_of(reader, dest):
    try:
        return reader.get_destination_page_number(dest) + 1  # 1-indexed
    except Exception:
        return None


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    reader = PyPDF2.PdfReader(PDF)
    total = len(reader.pages)
    print("total pages:", total)

    raw = walk(reader.outline)
    entries = []
    for d in raw:
        p = page_of(reader, d)
        entries.append((p, d.title))

    # Build ordered (page, title) list, keep only top-level markers we care about
    chapter_re = re.compile(r"^(\d+)\.\s")
    appendix_re = re.compile(r"^([AB])\.\s")
    part_re = re.compile(r"^[IVXLC]+\.\s")
    picks = []
    for p, t in entries:
        if (chapter_re.match(t) or appendix_re.match(t) or part_re.match(t) or t in (
                "Index", "About the Author", "Preface")):
            picks.append((p, t))
    picks.sort()

    # Derive ranges: each section spans [start, next_start-1]
    ranges = []
    for i, (p, t) in enumerate(picks):
        end = picks[i + 1][0] - 1 if i + 1 < len(picks) else total
        ranges.append((t, p, end))

    for t, p, end in ranges:
        if part_re.match(t) or t == "Preface":
            continue  # boundary-only: part divider / front matter
        if t.startswith("Index"):
            out = os.path.join(OUT_DIR, "index.txt")
        elif t.startswith("About the Author"):
            out = os.path.join(OUT_DIR, "about_the_author.txt")
        elif appendix_re.match(t):
            letter = appendix_re.match(t).group(1).lower()
            out = os.path.join(OUT_DIR, "appendix_%s.txt" % letter)
        elif chapter_re.match(t):
            m = chapter_re.match(t)
            num = int(m.group(1))
            out = OUT_DIR + os.sep + "ch%02d.txt" % num
        else:
            continue

        # page range sanity
        lo = max(p, 1)
        hi = min(end, total)
        body = []
        for pg in range(lo - 1, hi):
            tx = reader.pages[pg].extract_text() or ""
            if tx.strip():
                body.append(clean(tx))
        text = "\n\n".join(body)
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print("%-36s pages %d-%d  %8d chars" % (os.path.basename(out), lo, hi, len(text)))
    print("DONE")


if __name__ == "__main__":
    main()
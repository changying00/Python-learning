import sys
import re
import os

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import PyPDF2

PDF = "learning-python-powerful-6th.pdf"
OUT_DIR = "chapters"

# chapter start pages (1-indexed) from the prior scan
CHAPTER_STARTS = {
    1: 16, 2: 37, 3: 54, 4: 95, 5: 141, 6: 191, 7: 212, 8: 280,
    9: 331, 10: 389, 11: 414, 12: 461, 13: 491, 14: 527, 15: 560,
    16: 591, 17: 611, 18: 658, 19: 706, 20: 747, 21: 816, 22: 859,
    23: 883, 24: 909, 25: 944, 26: 988, 27: 1008, 28: 1035, 29: 1085,
    30: 1122, 31: 1181, 32: 1237, 33: 1322, 34: 1338, 35: 1378,
    36: 1403, 37: 1435, 38: 1499, 39: 1557, 40: 1641, 41: 1692,
}
NUM_PAGES = 1978  # one past last page marker


def clean(text):
    # calibre conversion inserted tabs between words; normalize
    text = text.replace("\t", " ")
    # collapse multiple spaces but keep newlines
    lines = []
    for ln in text.split("\n"):
        ln = re.sub(r"[ ]{2,}", " ", ln)
        lines.append(ln)
    return "\n".join(lines)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    reader = PyPDF2.PdfReader(PDF)
    total = len(reader.pages)
    print(f"total pages: {total}", flush=True)

    chapters = sorted(CHAPTER_STARTS.items())
    for idx, (num, start) in enumerate(chapters):
        end = (chapters[idx + 1][1] - 1) if idx + 1 < len(chapters) else NUM_PAGES
        end = min(end, total)
        parts = []
        for p in range(start - 1, end):
            t = reader.pages[p].extract_text() or ""
            if t.strip():
                parts.append(clean(t))
        body = "\n\n".join(parts)
        out = os.path.join(OUT_DIR, f"ch{num:02d}.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(body)
        print(f"ch{num:02d}: pages {start}-{end} -> {len(body)} chars", flush=True)

    print("DONE", flush=True)


if __name__ == "__main__":
    main()
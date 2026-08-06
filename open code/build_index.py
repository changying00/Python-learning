import sys
import re
import glob

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import fitz

PDF = "learning-python-powerful-6th.pdf"
DST = "chapters/index.md"
FIRST = 1806
LAST = 1976

GROUPS = ["Symbols"] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
GROUP_RE = re.compile(r"^(Symbols|[A-Z])$")
SEE_ALSO_RE = re.compile(r"\(\s*see\s+also[^)]*\)", re.IGNORECASE)
PUNCT_EDGES = re.compile(r"^[^\w\s]+|[^\w\s]+$")
UPPER_START = re.compile(r"^[A-Z]")
REF_STARTS = frozenset(
    "def lambda for while try except finally import from class if elif else in is not and or "
    "not pass return yield del global nonlocal raise with as assert break continue match case "
    "await async type print open dir map zip filter range input exec eval format id vars globals "
    "locals min max sum len abs round pow divmod ord chr bin oct hex bool int float str list dict "
    "set tuple frozenset bytes bytearray complex memoryview super property staticmethod classmethod "
    "isinstance getattr setattr hasattr callable help compile repr hash iter next all any".split()
)


def norm_words(token):
    if not token or not token.isalnum():
        pass
    stripped = PUNCT_EDGES.sub("", token).lower()
    if not stripped:
        return [token.lower()]
    out = []
    for part in stripped.split("-"):
        part = PUNCT_EDGES.sub("", part)
        if part:
            out.append(part)
    return out or [stripped]


def tokenize_line(text):
    text = SEE_ALSO_RE.sub(" ", text)
    out = []
    for raw in re.split(r"[ \t]+", text.strip()):
        nw = norm_words(raw)
        if nw:
            out.append((raw, nw))
    return out


def build_vocab():
    vocab = set()
    toc_one = set()
    doc = fitz.open(PDF)
    for lvl, title, page in doc.get_toc():
        nw = []
        for w in re.split(r"[, \t]+", title):
            nw.extend(norm_words(w))
        if nw:
            vocab.add(" ".join(nw))
        if len(nw) == 1:
            toc_one.add(nw[0])
    doc.close()
    for f in glob.glob("chapters/ch[0-9][0-9].txt") + glob.glob("chapters/appendix_*.txt"):
        for ln in open(f, encoding="utf-8"):
            s = ln.strip()
            if not s or len(s) < 3 or len(s) > 140:
                continue
            if not s[0].isupper():
                continue
            if s.startswith(("Chapter ", "Part ", "Figure ", "Table ", "Appendix", "Preface", "Index", "Colophon", "About the Author")):
                continue
            if re.search(r"[.!:;,]$", s):
                continue
            if "\t" in s:
                continue
            if re.match(r"^[A-Z\s]{2,}$", s):
                continue
            if "=" in s or "\\" in s:
                continue
            nw = []
            for w in re.split(r"[, \t]+", s):
                nw.extend(norm_words(w))
            if not nw:
                continue
            if len(nw) == 1 and nw[0] not in toc_one:
                continue
            vocab.add(" ".join(nw))
    return vocab


def page_lines(page):
    words = page.get_text("words")
    ls = {}
    for w in words:
        y = round(w[1], 0)
        ls.setdefault(y, []).append(w)
    out = []
    for y in sorted(ls):
        ws = sorted(ls[y], key=lambda w: w[0])
        out.append((ws[0][0], " ".join(w[4] for w in ws)))
    return out


class Buffer:
    def __init__(self, vocab):
        self.vocab = vocab
        self.maxlen = max(len(v.split()) for v in vocab) if vocab else 1
        self.pairs = []

    def add(self, toks):
        for raw, nw in toks:
            self.pairs.append([raw, list(nw)])

    def flat(self):
        out = []
        for raw, nw in self.pairs:
            out.extend(nw)
        return out

    def longest_match(self):
        flat = self.flat()
        end = min(len(flat), self.maxlen)
        for L in range(end, 0, -1):
            if " ".join(flat[:L]) in self.vocab:
                return L
        return 0

    def consume(self, L):
        emitted = []
        covered = 0
        while covered < L:
            raw, nw = self.pairs[0]
            n = len(nw)
            if n == 0:
                self.pairs.pop(0)
                continue
            if covered + n <= L:
                emitted.append(raw)
                self.pairs.pop(0)
                covered += n
            else:
                need = L - covered
                parts = [p for p in raw.split("-") if p]
                if len(parts) > need:
                    head = "-".join(parts[:need])
                    tail = "-".join(parts[need:])
                    emitted.append(head)
                    self.pairs[0] = [tail, list(nw[need:])]
                    covered = L
                else:
                    emitted.append(raw)
                    self.pairs.pop(0)
                    covered += n
        return " ".join(emitted).rstrip(", -").lstrip("- ")

    def longest_match_from(self, flat, pos):
        end = min(len(flat), pos + self.maxlen)
        for L in range(end - pos, 0, -1):
            if " ".join(flat[pos:pos + L]) in self.vocab:
                return L
        return None

    def word_count(self):
        return len(self.flat())

    def is_empty(self):
        return not any(nw for raw, nw in self.pairs)


def main():
    vocab = build_vocab()
    print("vocab size:", len(vocab), flush=True)

    doc = fitz.open(PDF)
    groups = {}
    current = None
    for p in range(FIRST - 1, LAST):
        for x0, text in page_lines(doc[p]):
            t = text.strip()
            if GROUP_RE.match(t):
                current = t
                groups.setdefault(current, [])
                continue
            if t == "Index":
                continue
            if current is None:
                continue
            groups[current].append((x0, t))

    out = []
    out.append("# 索引（Index）\n")
    out.append("> **原书**：《Learning Python》（6th Edition），作者 Mark Lutz。")
    out.append(">")
    out.append(
        "> 本页为原书书末索引（第 1806–1976 页）的逐条整理：每条索引按首字母分组，"
        "粗体为该索引词条，其后为该主题在书中的讨论章节/小节。"
    )
    out.append(">")
    out.append(
        "> **使用说明**：按字母顺序检索；词条后所列条目为书中讨论该主题的位置，"
        "可在对应章节笔记中查找。索引词条与位置名保留英文原样，以保持可检索性。\n"
    )

    total = 0
    for g in GROUPS:
        if g not in groups:
            continue
        out.append(f"## {g}\n")
        entries = []
        cur = None
        buf = Buffer(vocab)
        in_see_also = False
        prev_hyphen = False
        for x0, text in groups[g]:
            t = text.strip()
            if in_see_also:
                if t.endswith(")"):
                    in_see_also = False
                continue
            if t == "":
                continue
            if t == "(" or t.startswith("see also") or t.startswith("("):
                in_see_also = not t.endswith(")")
                continue
            toks = tokenize_line(t)
            if not toks:
                prev_hyphen = t.endswith("-")
                continue
            line_words = sum(len(nw) for _, nw in toks)
            if not buf.is_empty() or prev_hyphen:
                pre = buf.word_count()
                buf.add(toks)
                while True:
                    L = buf.longest_match()
                    if not L:
                        break
                    emitted = buf.consume(L)
                    if cur is not None:
                        cur["refs"].append(emitted)
                if buf.word_count() <= pre:
                    prev_hyphen = t.endswith("-")
                    continue
                if buf.word_count() > 0 and "," in t and x0 > 80:
                    buf = Buffer(vocab)
                elif buf.word_count() > 45:
                    emitted = buf.consume(buf.word_count())
                    if cur is not None and emitted:
                        cur["refs"].append(emitted)
            if not buf.is_empty() or prev_hyphen:
                prev_hyphen = t.endswith("-")
                continue
            i = 0
            term_words = []
            paren = 0
            field_done = False
            is_symbol = lambda r: bool(r) and not any(c.isalnum() for c in r)
            toks_raw = [t[0] for t in toks]
            n = len(toks_raw)
            while i < n:
                raw = toks_raw[i]
                opens = raw.count("(")
                closes = raw.count(")")
                nxt = toks_raw[i + 1] if i + 1 < n else ""
                if i == 0 or paren > 0:
                    term_words.append(raw)
                    paren = max(0, paren + opens - closes)
                    i += 1
                    if raw.endswith(","):
                        field_done = True
                    continue
                if is_symbol(raw):
                    if UPPER_START.match(nxt) or is_symbol(nxt):
                        break
                    term_words.append(raw)
                    i += 1
                    if raw.endswith(","):
                        field_done = True
                    continue
                if not field_done:
                    term_words.append(raw)
                    paren = max(0, paren + opens - closes)
                    i += 1
                    if raw.endswith(","):
                        field_done = True
                    continue
                if UPPER_START.match(raw) or raw.rstrip(",").lower() in REF_STARTS:
                    break
                term_words.append(raw)
                paren = max(0, paren + opens - closes)
                i += 1
            term = " ".join(term_words).rstrip(",")
            if not term:
                continue
            buf.add(toks[i:])
            refs = []
            while True:
                L = buf.longest_match()
                if not L:
                    break
                refs.append(buf.consume(L))
            entry = {"term": term, "refs": refs, "sub": x0 > 80}
            entries.append(entry)
            cur = entry
            total += 1
            prev_hyphen = t.endswith("-")
        for e in entries:
            refs = []
            for r in e["refs"]:
                if not refs or r != refs[-1]:
                    refs.append(r)
            tail = f"：{'；'.join(refs)}" if refs else ""
            if e["sub"]:
                out.append(f"    - **{e['term']}**{tail}")
            else:
                out.append(f"- **{e['term']}**{tail}")
        out.append("")
    out.append("---\n")
    out.append(f"*共收录 {total} 个索引词条，按 Symbols + A–Z 排列。*\n")
    open(DST, "w", encoding="utf-8").write("\n".join(out))
    print("written:", DST, "entries:", total)


if __name__ == "__main__":
    main()
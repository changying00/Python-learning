import os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = "chapters"

CHAPTERS = {
    37: {"en": "Unicode and Byte Strings", "zh": "Unicode\u4e0e\u5b57\u8282\u5b57\u7b26\u4e32",
         "pos": "\u7b2c37\u7ae0\u662f\u5b57\u7b26\u4e32\u5904\u7406\u7684\u9ad8\u7ea7\u7bc7\uff0c\u5728\u7b2c7\u7ae0\u57fa\u7840\u4e0a\u5c06\u5b57\u7b26\u4e32\u6a21\u578b\u6269\u5c55\u5230\u5b8c\u6574\u7684Unicode\u6587\u672c\u548c\u4e8c\u8fdb\u5236\u6570\u636e\u5904\u7406\u3002\u672c\u7ae0\u662fPython 3.x\u7684\u5fc5\u4fee\u5185\u5bb9\uff0c\u56e0\u4e3a\u6b63\u5e38\u5b57\u7b26\u4e32\u672c\u8eab\u5c31\u662fUnicode\u3002"},
    38: {"en": "Attributes and Methods", "zh": "\u5c5e\u6027\u4e0e\u65b9\u6cd5",
         "pos": "\u7b2c38\u7ae0\u6df1\u5165\u8bb2\u89e3Python\u7684\u5c5e\u6027\u7ba1\u7406\u673a\u5236\uff0c\u5305\u62ec__getattr__\u3001__getattribute__\u3001\u63cf\u8ff0\u7b26\u548c\u5c5e\u6027\u88c5\u9970\u5668\u3002\u8fd9\u662f\u7406\u89e3Python\u5bf9\u8c61\u6a21\u578b\u7684\u6838\u5fc3\u7ae0\u8282\u3002"},
    39: {"en": "Decorators", "zh": "\u88c5\u9970\u5668",
         "pos": "\u7b2c39\u7ae0\u8bb2\u89e3\u88c5\u9970\u5668\u2014\u2014\u5728\u51fd\u6570\u548c\u7c7b\u521b\u5efa\u65f6\u81ea\u52a8\u8fd0\u884c\u7684\u4ee3\u7801\u3002\u88c5\u9970\u5668\u662fPython\u6700\u5f3a\u5927\u7684\u5143\u7f16\u7a0b\u5de5\u5177\u4e4b\u4e00\uff0c\u5e7f\u6cdb\u5e94\u7528\u4e8e\u6846\u67b6\u548c\u5e93\u7684\u5f00\u53d1\u4e2d\u3002"},
    40: {"en": "Metaclasses", "zh": "\u5143\u7c7b",
         "pos": "\u7b2c40\u7ae0\u8bb2\u89e3\u5143\u7c7b\u2014\u2014\u521b\u5efa\u7c7b\u7684\u7c7b\u3002\u5143\u7c7b\u662fPython\u6700\u9ad8\u7ea7\u7684\u6982\u5ff5\u4e4b\u4e00\uff0c\u5b83\u4e0e\u7ee7\u627f\u3001\u63cf\u8ff0\u7b26\u548c\u88c5\u9970\u5668\u6df1\u5ea6\u7f29\u7f29\uff0c\u662f\u7406\u89e3Python\u5bf9\u8c61\u6a21\u578b\u7684\u5173\u952e\u3002"},
    41: {"en": "All Good Things", "zh": "\u7f8e\u597d\u7684\u7ec8\u7ed3",
         "pos": "\u7b2c41\u7ae0\u662f\u672c\u4e66\u7684\u6700\u540e\u4e00\u7ae0\uff0c\u56de\u987ePython\u7684\u53d1\u5c55\u5386\u7a0b\uff0c\u8ba8\u8bba\u5176\u53d8\u5316\u901f\u7387\uff0c\u5e76\u5c55\u671b\u672a\u6765\u3002\u4f5c\u4e3a\u6536\u5c3e\u7ae0\u8282\uff0c\u5b83\u603b\u7ed3\u5168\u4e66\u7684\u6838\u5fc3\u601d\u60f3\u3002"},
}


def read_txt(num):
    path = os.path.join("chapters", f"ch{num:02d}.txt")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_at(text, boundaries):
    sections = []
    prev_end = 0
    for start, title in boundaries:
        if start > prev_end:
            body = text[prev_end:start].strip()
            if body:
                sections.append((title, body))
        prev_end = start
    if prev_end < len(text):
        body = text[prev_end:].strip()
        if body:
            sections.append((text[prev_end:prev_end+80].strip() if prev_end == 0 else "Remaining Content", body))
    return sections


def clean_quote(text):
    return text.replace("\n", "\n> ")


def deep_understand(title, body):
    t = title.lower()
    if "unicode" in t or "character encod" in t or "byte string" in t or "utf-8" in t or "encoding" in t:
        return [
            "- **\u6838\u5fc3\u6982\u5ff5**\uff1aUnicode\u662f\u4e00\u79cd\u4e3a\u4e16\u754c\u4e0a\u6240\u6709\u4e66\u5199\u7cfb\u7edf\u7684\u6bcf\u4e2a\u5b57\u7b26\u5206\u914d\u552f\u4e00\u6570\u5b57\u7f16\u53f7\u7684\u901a\u7528\u7f16\u7801\u6807\u51c6\u3002Python 3\u4e2dstr\u5bf9\u8c61\u539f\u751f\u652f\u6301Unicode\uff0cbytes\u5bf9\u8c61\u5904\u7406\u539f\u59cb\u4e8c\u8fdb\u5236\u6570\u636e",
            "- **\u5e95\u5c42\u5b9e\u73b0**\uff1aPython\u7684str\u5bf9\u8c61\u5728\u5185\u90e8\u4f7f\u7528Unicode\u7f16\u7801\u5b58\u50a8\uff0cUTF-8\u662f\u9ed8\u8ba4\u7684\u6e90\u6587\u4ef6\u7f16\u7801\u3002\u6587\u672c\u6587\u4ef6\u901a\u8fc7open()\u7684encoding\u53c2\u6570\u5b9e\u73b0\u7f16\u89e3\u7801\uff0c\u5e95\u5c42\u8c03\u7528\u7684\u662fPython\u7684\u7f16\u89e3\u7801\u5668\u6846\u67b6",
            "- **\u8bbe\u8ba1\u539f\u56e0**\uff1aPython 3\u5c06Unicode\u4f5c\u4e3a\u5b57\u7b26\u4e32\u7684\u9ed8\u8ba4\u7f16\u7801\uff0c\u6d88\u9664\u4e86Python 2\u4e2dstr\u548cunicode\u7c7b\u578b\u7684\u6df7\u4e71\u3002\u8fd9\u79cd\u8bbe\u8ba1\u7b26\u5408\u73b0\u4ee3\u8f6f\u4ef6\u56fd\u9645\u5316\u7684\u9700\u6c42",
            "- **\u5b9e\u9645\u95ee\u9898**\uff1a\u8de8\u5e73\u53f0\u6587\u4ef6\u8bfb\u5199\u65f6\uff0c\u9ed8\u8ba4\u7f16\u7801\u53ef\u80fd\u4e0d\u540c\uff08Windows\u4e0a\u53ef\u80fd\u662fcp1252\uff0cmacOS/Linux\u4e0a\u662fUTF-8\uff09\uff0c\u5bfc\u81f4\u975eASCII\u5b57\u7b26\u5728\u4e0d\u540c\u5e73\u53f0\u95f4\u4f20\u8f93\u65f6\u51fa\u73b0\u4e71\u7801",
            "- **\u521d\u5b66\u8005\u8bef\u5ff5**\uff1a\u5f88\u591a\u4eba\u8ba4\u4e3aUTF-8\u548cUnicode\u662f\u4e00\u4e8b\u3002\u5b9e\u9645\u4e0aUnicode\u662f\u5b57\u7b26\u96c6\u6807\u51c6\uff0cUTF-8\u662f\u7f16\u7801\u65b9\u5f0f\uff1b\u4e00\u4e2aUnicode\u5b57\u7b26\u53ef\u4ee5\u6709\u591a\u79cdUTF\u7f16\u7801\u5f62\u5f0f",
        ]
    elif "attribute" in t or "method" in t or "getattr" in t or "getattribute" in t:
        return [
            "- **\u6838\u5fc3\u6982\u5ff5**\uff1aPython\u7684\u5c5e\u6027\u8bbf\u95ee\u4e0d\u662f\u7b80\u5355\u7684\u5b57\u5178\u67e5\u627e\uff0c\u800c\u662f\u7ecf\u8fc7\u591a\u5c42\u534f\u8bae\u5904\u7406\u7684\u590d\u6742\u8fc7\u7a0b\uff0c\u5305\u62ec__getattribute__\u3001__getattr__\u3001\u63cf\u8ff0\u7b26\u548c\u6570\u636e\u63cf\u8ff0\u7b26\u4f18\u5148\u7ea7\u89c4\u5219",
            "- **\u5e95\u5c42\u5b9e\u73b0**\uff1aPython\u7684\u5c5e\u6027\u67e5\u627e\u9075\u5faaMRO\uff08\u65b9\u6cd5\u89e3\u6790\u987a\u5e8f\uff09\uff0c\u5148\u5728\u5b9e\u4f8b\u7684__dict__\u4e2d\u67e5\u627e\uff0c\u7136\u540e\u6309\u7c7b\u7684MRO\u94fe\u67e5\u627e\uff0c\u6700\u540e\u89e6\u53d1__getattr__\u3002\u63cf\u8ff0\u7b26\u534f\u8bae\uff08__get__\u3001__set__\u3001__delete__\uff09\u5728\u67e5\u627e\u8fc7\u7a0b\u4e2d\u4f18\u5148\u4e8e\u5b9e\u4f8b\u5b57\u5178",
            "- **\u8bbe\u8ba1\u539f\u56e0**\uff1a\u63cf\u8ff0\u7b26\u534f\u8bae\u5c06\u5c5e\u6027\u7ba1\u7406\u7684\u903b\u8f91\u4ece\u5b9e\u4f8b\u4e2d\u5206\u79bb\u51fa\u6765\uff0c\u4f7f\u5f97\u5c5e\u6027\u53ef\u4ee5\u8de8\u7c7b\u590d\u7528\u3002\u5c5e\u6027\u88c5\u9970\u5668property\u5c31\u662f\u63cf\u8ff0\u7b26\u7684\u4e00\u4e2a\u7279\u4f8b",
            "- **\u5b9e\u9645\u95ee\u9898**\uff1a__getattr__\u548c__getattribute__\u7684\u9012\u5f52\u9677\u9631\u2014\u2014\u5728__getattribute__\u4e2d\u8bbf\u95eeself.xxx\u4f1a\u518d\u6b21\u89e6\u53d1__getattribute__\uff0c\u5fc5\u987b\u4f7f\u7528object.__getattribute__(self, 'xxx')\u6765\u907f\u514d",
            "- **\u521d\u5b66\u8005\u8bef\u5ff5**\uff1a\u5f88\u591a\u4eba\u8ba4\u4e3a__getattr__\u4f1a\u5728\u6240\u6709\u5c5e\u6027\u8bbf\u95ee\u65f6\u89e6\u53d1\uff0c\u5b9e\u9645\u4e0a\u5b83\u53ea\u5728\u5c5e\u6027\u672a\u627e\u5230\u65f6\u89e6\u53d1\uff1b\u800c__getattribute__\u4f1a\u5728\u6bcf\u6b21\u8bbf\u95ee\u65f6\u89e6\u53d1\uff0c\u4f46\u9700\u8981\u5c0a\u614e\u907f\u514d\u65e0\u9650\u9012\u5f52",
        ]
    elif "decorator" in t or "property" in t or "descriptor" in t or "validation" in t or "argument" in t or "range" in t:
        return [
            "- **\u6838\u5fc3\u6982\u5ff5**\uff1a\u88c5\u9970\u5668\u672c\u8d28\u4e0a\u662f\u4e00\u4e2a\u63a5\u53d7\u51fd\u6570\u6216\u7c7b\u4f5c\u4e3a\u53c2\u6570\u5e76\u8fd4\u56de\u65b0\u51fd\u6570\u6216\u7c7b\u7684\u53ef\u8c03\u7528\u5bf9\u8c61\u3002\u5b83\u5229\u7528Python\u7684\u95ed\u5305\u548c\u4f5c\u7528\u57df\u673a\u5236\uff0c\u5728\u51fd\u6570\u5b9a\u4e49\u65f6\u81ea\u52a8\u4fee\u6539\u51fd\u6570\u884c\u4e3a",
            "- **\u5e95\u5c42\u5b9e\u73b0**\uff1a\u5f53Python\u6267\u884c@decorator\u8bed\u6cd5\u65f6\uff0c\u5b83\u5b9e\u9645\u4e0a\u6267\u884c\u4e86func = decorator(func)\u3002\u88c5\u9970\u5668\u8fd4\u56de\u7684wrapper\u51fd\u6570\u901a\u8fc7\u95ed\u5305\u4fdd\u7559\u4e86\u539f\u59cb\u51fd\u6570\u7684\u53c2\u7167\u548c\u88c5\u9970\u5668\u53c2\u6570",
            "- **\u8bbe\u8ba1\u539f\u56e0**\uff1a\u88c5\u9970\u5668\u6a21\u5f0f\u5c06\u6a2a\u5207\u5173\u6ce8\u70b9\uff08\u5982\u65e5\u5fd7\u3001\u8ba1\u65f6\u3001\u6743\u9650\u6821\u9a8c\uff09\u4ece\u4e1a\u52a1\u903b\u8f91\u4e2d\u5206\u79bb\u51fa\u6765\uff0c\u4f7f\u5f97\u4ee3\u7801\u66f4\u6e05\u6670\u3001\u66f4\u53ef\u590d\u7528\u3002Python\u7684\u8bed\u6cd5\u7cd6\u4f7f\u88c5\u9970\u5668\u4f7f\u7528\u8d77\u6765\u975e\u5e38\u7b80\u6d01",
            "- **\u5b9e\u9645\u95ee\u9898**\uff1a\u88c5\u9970\u5668\u4f1a\u6539\u53d8\u51fd\u6570\u7684\u5143\u4fe1\u606f\uff08\u5982__name__\u3001__doc__\uff09\uff0c\u9700\u8981\u4f7f\u7528functools.wraps\u6765\u4fdd\u7559\u539f\u59cb\u51fd\u6570\u7684\u5c5e\u6027\u3002\u8fd9\u5728\u8c03\u8bd5\u548c\u6587\u6863\u751f\u6210\u65f6\u975e\u5e38\u91cd\u8981",
            "- **\u521d\u5b66\u8005\u8bef\u5ff5**\uff1a\u5f88\u591a\u4eba\u8ba4\u4e3a\u88c5\u9970\u5668\u53ea\u5728\u51fd\u6570\u8c03\u7528\u65f6\u6267\u884c\uff0c\u5b9e\u9645\u4e0a\u88c5\u9970\u5668\u5728\u51fd\u6570\u5b9a\u4e49\u65f6\u5c31\u6267\u884c\u4e86\uff08@\u8bed\u6cd5\u5728import\u65f6\u5c31\u4f1a\u8fd0\u884c\uff09\u3002\u88c5\u9970\u5668\u7684\u53c2\u6570\u662f\u5728\u5b9a\u4e49\u65f6\u786e\u5b9a\u7684\uff0c\u4e0d\u662f\u5728\u8c03\u7528\u65f6",
        ]
    elif "metaclass" in t or "inheritance" in t or "MRO" in t or "type" in t:
        return [
            "- **\u6838\u5fc3\u6982\u5ff5**\uff1a\u5143\u7c7b\u662f\u521b\u5efa\u7c7b\u7684\u7c7b\u3002\u5728Python\u4e2d\uff0ctype\u662f\u6240\u6709\u7c7b\u7684\u9ed8\u8ba4\u5143\u7c7b\uff0c\u7c7b\u672c\u8eab\u5c31\u662ftype\u7684\u5b9e\u4f8b\u3002\u5143\u7c7b\u5141\u8bb8\u5728\u7c7b\u521b\u5efa\u65f6\u81ea\u5b9a\u4e49\u7c7b\u7684\u884c\u4e3a",
            "- **\u5e95\u5c42\u5b9e\u73b0**\uff1a\u5f53Python\u6267\u884cclass\u8bed\u53e5\u65f6\uff0c\u5b83\u9996\u5148\u6536\u96c6\u7c7b\u5b57\u5178\uff0c\u7136\u540e\u8c03\u7528\u6307\u5b9a\u7684\u5143\u7c7b\uff08\u9ed8\u8ba4\u662ftype\uff09\u7684__new__\u548c__init__\u65b9\u6cd5\u6765\u521b\u5efa\u7c7b\u5bf9\u8c61\u3002\u5143\u7c7b\u7684__new__\u65b9\u6cd5\u63a5\u6536\u7c7b\u540d\u3001\u7236\u7c7b\u5217\u8868\u548c\u7c7b\u5b57\u5178\u4f5c\u4e3a\u53c2\u6570",
            "- **\u8bbe\u8ba1\u539f\u56e0**\uff1a\u5143\u7c7b\u63d0\u4f9b\u4e86\u4e00\u79cd\u5728\u7c7b\u521b\u5efa\u65f6\u6ce8\u5165\u4ee3\u7801\u7684\u673a\u5236\uff0c\u8fd9\u5728ORM\u6846\u67b6\u3001API\u6ce8\u518c\u3001\u63a5\u53e3\u9a8c\u8bc1\u7b49\u573a\u666f\u4e2d\u975e\u5e38\u6709\u7528\u3002\u5b83\u6bd4\u7c7b\u88c5\u9970\u5668\u66f4\u5e95\u5c42\uff0c\u56e0\u4e3a\u5143\u7c7b\u63a7\u5236\u7684\u662f\u7c7b\u7684\u521b\u5efa\u8fc7\u7a0b\u672c\u8eab",
            "- **\u5b9e\u9645\u95ee\u9898**\uff1a\u5143\u7c7b\u7684\u7ee7\u627f\u884c\u4e3a\u590d\u6742\u2014\u2014\u5143\u7c7b\u58f0\u660e\u4f1a\u88ab\u5b50\u7c7b\u7ee7\u627f\uff0c\u8fd9\u53ef\u80fd\u5bfc\u81f4\u610f\u5916\u7684\u5143\u7c7b\u51b2\u7a81\u3002\u5f53\u7236\u7c7b\u6709\u4e0d\u540c\u7684\u5143\u7c7b\u65f6\uff0cPython\u4f1a\u5c1d\u8bd5\u81ea\u52a8\u5408\u5e76\u5b83\u4eec",
            "- **\u521d\u5b66\u8005\u8bef\u5ff5**\uff1a\u5f88\u591a\u4eba\u8ba4\u4e3a\u5143\u7c7b\u7528\u4e8e\u63a7\u5236\u7c7b\u7684\u5b9e\u4f8b\uff0c\u5b9e\u9645\u4e0a\u5143\u7c7b\u63a7\u5236\u7684\u662f\u7c7b\u672c\u8eab\u3002\u5143\u7c7b\u5b9a\u4e49\u7684\u65b9\u6cd5\u53ea\u80fd\u901a\u8fc7\u7c7b\u8bbf\u95ee\uff0c\u4e0d\u80fd\u901a\u8fc7\u5b9e\u4f8b\u8bbf\u95ee\uff08\u8fd9\u662f\u4e0e\u666e\u901a\u7c7b\u65b9\u6cd5\u7684\u6839\u672c\u533a\u522b\uff09",
        ]
    else:
        return [
            "- **\u6838\u5fc3\u6982\u5ff5**\uff1a\u672c\u7ae0\u5185\u5bb9\u6d89\u53caPython\u7684\u6838\u5fc3\u673a\u5236\uff0c\u7406\u89e3\u8fd9\u4e9b\u6982\u5ff5\u5bf9\u4e8e\u6df1\u5165\u638c\u63e1Python\u81f3\u5173\u91cd\u8981",
            "- **\u5e95\u5c42\u5b9e\u73b0**\uff1aPython\u7684\u5185\u90e8\u5b9e\u73b0\u6d89\u53caC\u8bed\u8a00\u5c42\u9762\u7684\u5bf9\u8c61\u6a21\u578b\uff0c\u7406\u89e3\u8fd9\u4e9b\u5b9e\u73b0\u6709\u52a9\u4e8e\u7f16\u5199\u66f4\u9ad8\u6548\u7684\u4ee3\u7801",
            "- **\u8bbe\u8ba1\u539f\u56e0**\uff1aPython\u7684\u8bbe\u8ba1\u54f2\u5b66\u5f3a\u8c03\u53ef\u8bfb\u6027\u548c\u7b80\u6d01\u6027\uff0c\u8fd9\u4e9b\u673a\u5236\u7684\u8bbe\u8ba1\u90fd\u9075\u5faa\u4e86\u8fd9\u4e00\u539f\u5219",
            "- **\u5b9e\u9645\u95ee\u9898**\uff1a\u5728\u5b9e\u9645\u5f00\u53d1\u4e2d\uff0c\u6b63\u786e\u4f7f\u7528\u8fd9\u4e9b\u9ad8\u7ea7\u7279\u6027\u53ef\u4ee3\u8868\u663e\u63d0\u5347\u4ee3\u7801\u7684\u8d28\u91cf\u548c\u53ef\u7ef4\u62a4\u6027",
            "- **\u521d\u5b66\u8005\u8bef\u5ff5**\uff1a\u521d\u5b66\u8005\u5f80\u5f80\u8bd5\u56fe\u8fc7\u65e9\u4f7f\u7528\u8fd9\u4e9b\u9ad8\u7ea7\u7279\u6027\uff0c\u800c\u5ffd\u89c6\u4e86\u57fa\u7840\u77e5\u8bc6\u7684\u59ff\u575a\u638c\u63e1",
        ]


def learning_advice(num):
    m = {
        37: ("4/5", "\u638c\u63e1Unicode\u7f16\u7801\u539f\u7406\u3001str\u548cbytes\u7684\u533a\u522b\u3001\u6587\u4ef6\u7f16\u7801\u53c2\u6570\u7684\u4f7f\u7528", "\u5b66\u4e60\u7b2c8\u7ae0\u7684\u5c5e\u6027\u7ba1\u7406\u3001\u7b2c39\u7ae0\u7684\u88c5\u9970\u5668"),
        38: ("5/5", "\u6df1\u5165\u7406\u89e3\u5c5e\u6027\u8bbf\u95ee\u534f\u8bae\u3001\u63cf\u8ff0\u7b26\u534f\u8bae\u3001property\u548c__getattr__/__getattribute__\u7684\u533a\u522b\u4e0e\u8054\u7cfb", "\u5b66\u4e60\u7b2c39\u7ae0\u7684\u88c5\u9970\u5668"),
        39: ("5/5", "\u638c\u63e1\u88c5\u9970\u5668\u7684\u7f16\u5199\u3001\u53c2\u6570\u4f20\u9012\u3001\u5d4c\u5957\u4f7f\u7528\uff0c\u4ee5\u53ca\u88c5\u9970\u5668\u5728\u6846\u67b6\u8bbe\u8ba1\u4e2d\u7684\u5b9e\u9645\u5e94\u7528", "\u5b66\u4e60\u7b2c40\u7ae0\u7684\u5143\u7c7b"),
        40: ("4/5", "\u7406\u89e3\u5143\u7c7b\u7684\u57fa\u672c\u6982\u5ff5\u3001\u58f0\u660e\u65b9\u5f0f\u3001\u7ee7\u627f\u89c4\u5219\uff0c\u4ee5\u53ca\u5143\u7c7b\u4e0e\u7ee7\u627f\u7684\u5173\u7cfb", "\u5b66\u4e60\u7b2c41\u7ae0\u7684\u603b\u7ed3\u5185\u5bb9"),
        41: ("3/5", "\u4e86\u89e3Python\u7684\u53d1\u5c55\u5386\u53f2\u548c\u53d8\u5316\u8d8b\u52bf\uff0c\u5bf9\u5168\u4e66\u5185\u5bb9\u8fdb\u884c\u56de\u987e\u548c\u603b\u7ed3", "\u5f00\u59cb\u5b9e\u9645\u9879\u76ee\u5f00\u53d1"),
    }
    return m.get(num, ("3/5", "\u7406\u89e3\u672c\u7ae0\u6838\u5fc3\u6982\u5ff5", "\u7ee7\u7eed\u5b66\u4e60\u540e\u7eed\u7ae0\u8282"))


def tech_expansion(num):
    m = {
        37: {"app": "Unicode\u5904\u7406\u662f\u73b0\u4ee3\u8f6f\u4ef6\u5f00\u53d1\u7684\u57fa\u7840\u9700\u6c42\u2014\u2014Web\u5f00\u53d1\u4e2d\u7684\u56fd\u9645\u5316(i18n)\u3001API\u5f00\u53d1\u4e2d\u7684JSON\u7f16\u7801\u3001\u6587\u4ef6\u5904\u7406\u4e2d\u7684\u7f16\u7801\u8f6c\u6362\u7b49\u90fd\u9760Unicode\u77e5\u8bc6",
             "comp": "| \u7279\u6027 | Python | Java | C++ |\n|---|---|---|---|\n| \u5b57\u7b26\u4e32\u7c7b\u578b | str(Unicode) + bytes | String(Unicode) | char*/wstring |\n| \u9ed8\u8ba4\u7f16\u7801 | UTF-8 | UTF-16 | \u4f9d\u8d56\u5e73\u53f0 |\n| \u6587\u4ef6\u7f16\u7801 | open(encoding=...) | InputStreamReader | \u9700\u7b2c\u4e09\u65b9\u5e93 |\n| \u5b57\u8282\u4e32\u7c7b\u578b | bytes/bytearray | byte[] | char[] |",
             "hist": "Unicode\u6807\u51c6\u4ece1991\u5e74\u5f00\u59cb\u5236\u5b9a\uff0cPython 2.x\u4e2dstr\u548cunicode\u662f\u5206\u5f00\u7684\u7c7b\u578b\uff0cPython 3.x\u7edf\u4e00\u4e3astr=Unicode\u3002Python 3.3+\u5f15\u5165\u4e86PEP 393 flexible string representation",
             "adv": "\u6df1\u5165\u5b66\u4e60\uff1acodecs\u6a21\u5757\u3001locale\u6a21\u5757\u3001sys.getfilesystemencoding()\u3001PEP 393\u3001PEP 597(UTF-8 mode)"},
        38: {"app": "\u5c5e\u6027\u7ba1\u7406\u673a\u5236\u662fORM\u6846\u67b6(\u5982SQLAlchemy)\u3001\u6570\u636e\u9a8c\u8bc1\u5e93(\u5982Pydantic)\u3001\u4ee3\u7406\u6a21\u5f0f\u5b9e\u73b0\u7684\u6838\u5fc3\u6280\u672f",
             "comp": "| \u7279\u6027 | property | descriptor | __getattr__ |\n|---|---|---|---|\n| \u4f5c\u7528\u8303\u56f4 | \u5355\u4e2a\u5c5e\u6027 | \u5355\u4e2a\u5c5e\u6027 | \u6240\u6709\u672a\u5b9a\u4e49\u5c5e\u6027 |\n| \u662f\u5426\u53ef\u590d\u7528 | \u5426(\u7ed1\u5b9a\u5230\u7c7b) | \u662f(\u72ec\u7acb\u7c7b) | \u662f(\u65b9\u6cd5\u7ea7\u522b) |\n| \u662f\u5426\u62e6\u622a\u8d4b\u503c | \u662f(\u901a\u8fc7setter) | \u662f(\u901a\u8fc7__set__) | \u5426(\u9700\u914d\u5408__setattr__) |\n| \u663e\u793a\u5728dir()\u4e2d | \u662f | \u662f | \u5426 |\n| \u6027\u80fd | \u9ad8 | \u9ad8 | \u4e2d |",
             "hist": "\u63cf\u8ff0\u7b26\u534f\u8bae\u4ecePython 2.2\u5f15\u5165\uff0c\u662fPython 2.x\u65b0\u5f0f\u7c7b(new-style class)\u7684\u6838\u5fc3\u7279\u6027\u4e4b\u4e00\u3002property\u88c5\u9970\u5668\u4ecePython 2.6\u5f00\u59cb\u652f\u6301@\u8bed\u6cd5",
             "adv": "\u6df1\u5165\u5b66\u4e60\uff1a__slots__\u3001__getstate__/__setstate__(pickle\u534f\u8bae)\u3001__reduce__\u3001\u6570\u636e\u7c7b(dataclass)\u7684field\u63cf\u8ff0\u7b26\u3001typing.NamedTuple"},
        39: {"app": "\u88c5\u9970\u5668\u5e7f\u6cdb\u5e94\u7528\u4e8eWeb\u6846\u67b6(Django/Flask\u8def\u7531\u88c5\u9970\u5668)\u3001\u6d4b\u8bd5\u6846\u67b6(pytest.mark)\u3001\u5f02\u6b65(async/await)\u3001\u7c7b\u578b\u68c0\u67e5(@overload)\u3001\u7f13\u5b58(@lru_cache)\u7b49",
             "comp": "| \u7279\u6027 | \u51fd\u6570\u88c5\u9970\u5668 | \u7c7b\u88c5\u9970\u5668 | \u5143\u7c7b |\n|---|---|---|---|\n| \u4f5c\u7528\u5bf9\u8c61 | \u51fd\u6570/\u65b9\u6cd5 | \u7c7b | \u7c7b |\n| \u6267\u884c\u65f6\u673a | \u51fd\u6570\u5b9a\u4e49\u65f6 | \u7c7b\u5b9a\u4e49\u65f6 | \u7c7b\u5b9a\u4e49\u65f6 |\n| \u8fd4\u56de\u503c | \u65b0\u51fd\u6570 | \u65b0\u7c7b | \u65b0\u7c7b |\n| \u7075\u6d3b\u6027 | \u9ad8 | \u6700\u9ad8 | \u9ad8 |\n| \u590d\u6742\u5ea6 | \u4f4e | \u4e2d | \u9ad8 |",
             "hist": "Python 2.4\u5f15\u5165\u4e86\u51fd\u6570\u88c5\u9970\u5668\u8bed\u6cd5(@)\uff0cPython 2.6\u6269\u5c55\u4e86\u7c7b\u88c5\u9970\u5668\uff0cPEP 318\u548cPEP 3129\u5b9a\u4e49\u4e86\u88c5\u9970\u5668\u89c4\u8303",
             "adv": "\u6df1\u5165\u5b66\u4e60\uff1afunctools.wraps\u3001functools.lru_cache\u3001contextlib.contextmanager\u3001typing.overload\u3001__init_subclass__"},
        40: {"app": "\u5143\u7c7b\u5728ORM\u6846\u67b6(Django models)\u3001API\u6ce8\u518c(Flask\u8def\u7531)\u3001\u63a5\u53e3\u9a8c\u8bc1\u3001\u5e8f\u5217\u5316\u5e93\u7b49\u4e2d\u6709\u91cd\u8981\u5e94\u7528",
             "comp": "| \u7279\u6027 | \u7c7b\u88c5\u9970\u5668 | \u5143\u7c7b |\n|---|---|---|\n| \u63a7\u5236\u65f6\u673a | \u7c7b\u521b\u5efa\u540e | \u7c7b\u521b\u5efa\u65f6 |\n| \u4fee\u6539\u80fd\u529b | \u53ea\u80fd\u66ff\u6362\u6574\u4e2a\u7c7b | \u53ef\u4ee5\u4fee\u6539\u7c7b\u5b57\u5178 |\n| \u7ee7\u627f | \u4e0d\u81ea\u52a8\u7ee7\u627f | \u81ea\u52a8\u7ee7\u627f |\n| \u7528\u9014 | \u7b80\u5355\u589e\u5f3a | \u6846\u67b6\u7ea7\u5b9a\u5236 |\n| \u590d\u6742\u5ea6 | \u4f4e | \u9ad8 |",
             "hist": "\u5143\u7c7b\u6982\u5ff5\u4ecePython 2.2\u5f15\u5165\uff0cPEP 3115(2006)\u6807\u51c6\u5316\u4e86\u5143\u7c7b\u58f0\u660e\u8bed\u6cd5(metaclass=\u5173\u952e\u5b57)\uff0cPython 3\u4e2d\u5143\u7c7b\u6210\u4e3a\u6807\u51c6\u7279\u6027",
             "adv": "\u6df1\u5165\u5b66\u4e60\uff1atype.__new__\u3001__init_subclass__\u3001abc.ABCMeta\u3001typing.Generic\u3001__class_getitem__"},
        41: {"app": "\u7406\u89e3Python\u7684\u6f14\u53d8\u6709\u52a9\u4e8e\u9884\u6d4b\u672a\u6765\u8d8b\u52bf\uff0c\u505a\u51fa\u6280\u672f\u9009\u578b\u51b3\u7b56",
             "comp": "| Python\u7248\u672c | \u91cd\u8981\u7279\u6027 | \u53d1\u5e03\u5e74\u4efd |\n|---|---|---|\n| Python 2.0 | List comprehensions, GC | 2000 |\n| Python 2.4 | Decorators | 2004 |\n| Python 3.0 | Unicode by default, print() | 2008 |\n| Python 3.5 | Async/await | 2015 |\n| Python 3.6 | f-strings, variable annotations | 2016 |\n| Python 3.8 | Walrus operator, positional-only args | 2019 |\n| Python 3.10 | Structural pattern matching | 2021 |\n| Python 3.12 | Exception groups, type params | 2023 |",
             "hist": "Python\u7531Guido van Rossum\u4e8e1989\u5e74\u5723\u8bde\u8282\u671f\u95f4\u5f00\u59cb\u5f00\u53d1\uff0c1991\u5e74\u53d1\u5e03\u7b2c\u4e00\u4e2a\u516c\u5f00\u7248\u672c\u3002Python\u7684\u540d\u5b57\u6765\u6e90\u4e8eBBC\u559c\u5267\u8282\u76eeMonty Python's Flying Circus",
             "adv": "\u6df1\u5165\u5b66\u4e60\uff1aPython\u7684\u6f14\u8fdb\u8def\u7ebf\u56fe(PEP\u6d41\u7a0b)\u3001Python\u8f6f\u4ef6\u57fa\u91d1\u4f1a(PSF)\u3001\u6838\u5fc3\u5f00\u53d1\u6d41\u7a0b\u3001PEP 8\u98ce\u683c\u6307\u5357"},
    }
    return m.get(num, {"app": "", "comp": "", "hist": "", "adv": ""})


def chapter_summary(num):
    adv = learning_advice(num)
    exp = tech_expansion(num)
    return f"""# \u672c\u7ae0\u603b\u7ed3

## \u6280\u672f\u6269\u5c55\uff08Technical Expansion\uff09
- \u5b9e\u9645\u9879\u76ee\u4e2d\u7684\u5e94\u7528\u573a\u666f
{exp['app']}
- \u4e0e\u5176\u4ed6\u8bed\u8a00\uff08Java/C++\uff09\u7684\u533a\u522b\uff08\u53ef\u7528\u8868\u683c\uff09
{exp['comp']}
- Python \u53d1\u5c55\u5386\u53f2\u80cc\u666f
{exp['hist']}
- \u9ad8\u7ea7\u5f00\u53d1\u8005\u9700\u8981\u638c\u63e1\u7684\u76f8\u5173\u77e5\u8bc6
{exp['adv']}

## \u5b66\u4e60\u5efa\u8bae\uff08Learning Advice\uff09
- \u91cd\u8981\u7a0b\u5ea6\uff08{adv[0]}\uff09
- \u5e94\u8be5\u638c\u63e1\u5230\u4ec0\u4e48\u7a0b\u5ea6
{adv[1]}
- \u540e\u7eed\u5e94\u8be5\u5b66\u4e60\u54ea\u4e9b\u76f8\u5173\u5185\u5bb9
{adv[2]}
"""


def process_chapter(num):
    meta = CHAPTERS[num]
    text = read_txt(num)
    if text is None:
        print(f"SKIP ch{num:02d}.txt not found")
        return

    # Define section boundaries based on analysis
    if num == 37:
        boundaries = [
            (0, "Chapter Introduction"),
            (7569, "Character Encodings"),
            (73569, "Unicode, Bytes, and Other String Tools"),
            (87004, "UNICODE DEFAULTS AND UTF-8 MODE"),
            (90215, "The Unicode Twilight Zone"),
            (90724, "Dropping the BOM in Python"),
            (92085, "Making BOMs in Text Editors"),
            (96233, "Making BOMs in Python"),
            (100221, "Unicode Normalization: Whither Standard?"),
            (105571, "Chapter Summary"),
            (106650, "Test Your Knowledge: Quiz"),
            (107367, "Test Your Knowledge: Answers"),
        ]
    elif num == 38:
        boundaries = [
            (0, "Chapter Introduction"),
            (5237, "Properties"),
            (14383, "Descriptors"),
            (47837, "Generic Attribute Management"),
            (61014, "Intercepting Built-in Operations"),
            (91210, "Chapter Summary"),
            (91826, "Test Your Knowledge: Quiz"),
            (text.find("Test Your Knowledge: Answers"), "Test Your Knowledge: Answers"),
        ]
    elif num == 39:
        boundaries = [
            (0, "Chapter Introduction"),
            (text.find("What's a Decorator?"), "What's a Decorator?"),
            (text.find("Function Decorator Basics"), "Function Decorator Basics"),
            (text.find("Class Decorator Basics"), "Class Decorator Basics"),
            (text.find("Decorator Nesting"), "Decorator Nesting"),
            (text.find("Decorator Arguments"), "Decorator Arguments"),
            (text.find("Adding Decorator Arguments"), "Adding Decorator Arguments"),
            (text.find("Coding Function Decorators"), "Coding Function Decorators"),
            (text.find("Class decorators provide"), "Class Decorators in Depth"),
            (text.find("Example: Private and Public"), "Example: Private and Public Attributes"),
            (text.find("Implementation Details II"), "Implementation Details II"),
            (text.find("Workaround: Coding operator-overloading"), "Workaround: Built-in Operations"),
            (text.find("Example: Validating Function Arguments"), "Example: Validating Function Arguments"),
            (text.find("Open Issues"), "Open Issues"),
            (text.find("Decorator Arguments Versus Function Annotations"), "Decorator Arguments vs Annotations"),
            (138274, "Chapter Summary"),
            (139742, "Test Your Knowledge: Quiz"),
            (text.find("Test Your Knowledge: Answers"), "Test Your Knowledge: Answers"),
        ]
    elif num == 40:
        boundaries = [
            (0, "Chapter Introduction"),
            (text.find("Metaclass"), "Metaclass Basics"),
            (text.find("Metaclass Methods"), "Metaclass Methods"),
            (text.find("Metaclass Methods Versus Class Methods"), "Metaclass Methods vs Class Methods"),
            (text.find("Metaclass Methods Versus Instance Methods"), "Metaclass Methods vs Instance Methods"),
            (text.find("Inheritance: The Finale"), "Inheritance: The Finale"),
            (text.find("Metaclass Versus Superclass"), "Metaclass Versus Superclass"),
            (text.find("Metaclass Inheritance"), "Metaclass Inheritance"),
            (text.find("Python Inheritance Algorithm"), "Python Inheritance Algorithm"),
            (text.find("The descriptors deviation"), "The Descriptors Deviation"),
            (text.find("The assignment addendum"), "The Assignment Addendum"),
            (text.find("The super supplement"), "The super supplement"),
            (text.find("The built-ins bifurcation"), "The Built-ins Bifurcation"),
            (text.find("The Inheritance Wrap-Up"), "The Inheritance Wrap-Up"),
            (text.find("Metaclass Methods"), "Metaclass Methods (detailed)"),
            (text.find("Operator Overloading in Metaclass Methods"), "Operator Overloading in Metaclass Methods"),
            (text.find("Metaclass Methods Versus Instance Methods"), "Metaclass Methods vs Instance Methods (detailed)"),
            (86058, "Chapter Summary"),
            (87431, "Test Your Knowledge: Quiz"),
            (text.find("Test Your Knowledge: Answers"), "Test Your Knowledge: Answers"),
        ]
    elif num == 41:
        boundaries = [
            (0, "Chapter Introduction"),
            (text.find("The Python Tsunami"), "The Python Tsunami"),
            (text.find("Twelve years ago"), "Python's Rate of Change"),
            (text.find("All Good Things"), "All Good Things"),
            (text.find("About the Author"), "About the Author"),
            (text.find("Colophon"), "Colophon"),
            (text.find("Test Your Knowledge"), "Test Your Knowledge"),
        ]
    else:
        boundaries = [(0, "Chapter Introduction")]

    # Clean up boundaries: remove duplicates and sort
    seen = set()
    clean_boundaries = []
    for start, title in boundaries:
        if start < 0:
            continue
        if start in seen:
            continue
        seen.add(start)
        clean_boundaries.append((start, title))
    clean_boundaries.sort()

    sections = split_at(text, clean_boundaries)

    md = []
    md.append(f"# \u7b2c{num}\u7ae0\uff1a{meta['en']}\uff08{meta['zh']}\uff09")
    md.append("")
    md.append("> **\u539f\u4e66**\uff1a\u300aLearning Python\u300b\uff086th Edition\uff09\uff0c\u4f5c\u8005 Mark Lutz")
    md.append(f"> **\u672c\u7ae0\u5730\u4f4d**\uff1a{meta['pos']}")
    md.append("---")
    md.append("")

    for sec_title, sec_body in sections:
        if len(sec_body.strip()) < 30:
            continue

        md.append(f"## {sec_title}")
        md.append("")

        # Check if body has subsections
        subsections = re.split(r"\n(?=\d+\.\d+\s+)", sec_body)
        if len(subsections) > 1:
            for sub in subsections:
                sub = sub.strip()
                if not sub:
                    continue
                m = re.match(r"^(\d+\.\d+)\s+(.+)", sub)
                if m:
                    sub_head = f"{m.group(1)} {m.group(2)}"
                    sub_body = sub[m.end():].strip()
                else:
                    sub_head = sec_title
                    sub_body = sub

                md.append(f"### {sub_head}")
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u82f1\u6587\u539f\u6587\u2014\u2014\u2014\u2014")
                md.append("")
                md.append("> " + clean_quote(sub_body))
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u4e2d\u6587\u7ffb\u8bd1\u2014\u2014\u2014\u2014")
                md.append("")
                md.append("> [\u5f85\u7ffb\u8bd1]")
                md.append("")
                md.append("\u2014\u2014\u2014\u2014\u6df1\u5ea6\u7406\u89e3\u2014\u2014\u2014\u2014")
                md.append("")
                for p in deep_understand(sub_head, sub_body):
                    md.append(p)
                md.append("")
        else:
            md.append("\u2014\u2014\u2014\u2014\u82f1\u6587\u539f\u6587\u2014\u2014\u2014\u2014")
            md.append("")
            md.append("> " + clean_quote(sec_body))
            md.append("")
            md.append("\u2014\u2014\u2014\u2014\u4e2d\u6587\u7ffb\u8bd1\u2014\u2014\u2014\u2014")
            md.append("")
            md.append("> [\u5f85\u7ffb\u8bd1]")
            md.append("")
            md.append("\u2014\u2014\u2014\u2014\u6df1\u5ea6\u7406\u89e3\u2014\u2014\u2014\u2014")
            md.append("")
            for p in deep_understand(sec_title, sec_body):
                md.append(p)
            md.append("")

        md.append("---")
        md.append("")

    md.append(chapter_summary(num))

    md_path = os.path.join("chapters", f"ch{num:02d}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"ch{num:02d}: {len(text)} chars -> {md_path} ({len(sections)} sections)")


def main():
    for n in range(37, 42):
        process_chapter(n)
    print("DONE")


if __name__ == "__main__":
    main()
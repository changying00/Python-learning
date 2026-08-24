import re

text = """<div class="book">
    <a href="/book/1001">Python入门</a>
    <a href="/book/1002">Python进阶</a>
    <a href="/book/1003">Python实战</a>
    </div>
    """

regex=  r'<a\s+href="(.*?)">(.*?)</a>'
result = re.findall(regex, text)
for item in result:
    print(item[0],item[1])

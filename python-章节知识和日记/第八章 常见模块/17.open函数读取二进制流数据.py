"""

以 流的方式 读取数据 适用于 任意类型的文件 

"""
import base64

# 定义一个路径 、用来表示一张图片 
file = r"C:\Users\Administrator\Pictures\5234371a-c77a-485b-8653-1fac3ae639dc.png"

# 创建一个 字节流通道 
#  使用 字节流 读取文件 、不允许设置 字符集编码 
f = open(file, "rb") 

# 1. 一次性读取到 内存中 
# print(f.read())

# 2. 一次性 读取 指定 长度的内容到 内存中 
content = b""
# 一次读取 8kb 
while (bytes_img := f.read(8 << 10)) != b"":
    # print("======================================")
    content += bytes_img 

# 对 图片进行 base64 编码 
img_base64 = base64.b64encode(content).decode()

img_url = "data:image/png;base64," + img_base64

# 将 结果 写入到 网页中  img 标签 
html_temp = f"""
<img src="{img_url}"/>
"""

s = open("./img.html", "wt", encoding="utf-8")

s.write(html_temp)

s.close()

# 关闭通道 
f.close()
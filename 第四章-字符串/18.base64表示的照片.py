import base64

# 定义一个变量，存储一个 本地图片路径
img_path = r"C:\Users\Administrator\Desktop\c3b72a486f645aac583a6c29876af7ad.webp"

# 使用 open 函数 读取图片内容到 内存中 、返回 一个二进制流数据
with open(img_path, "rb") as f:
    img_bytes = f.read()

# 将 表示 图片的二进制流 进行 base64编码
img_decode = base64.b64encode(img_bytes).decode()

#  <img src=""/>
# 定义一个 表示 图片的 前缀
img_prefix = "data:image/jpeg;base64,"

img_url = img_prefix + img_decode

with open("test.html", "wt") as f:

    f.write(f'<img src="{img_url}"/>')

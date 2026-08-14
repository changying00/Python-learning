"""
  无论是 读操作 还是 写 操作 、都需要 打开文件通道 、且 使用完成后 关闭文件通道 

资源预处理模式 : 针对 某种特定的操作 例如 打开 一阵子后 需要关闭 这种 操作 

将 打开的操作 使用 with 定义 

"""

with open("./xxx.txt", "wb") as f:
    # 写入流数据 
    f.write(b"hello world!")
    # 如果 写入的 内容 全部是 ascii 字符、也可以直接在前面 添加 前缀 b
    f.write(b"\n")
    f.write("你好中国".encode())

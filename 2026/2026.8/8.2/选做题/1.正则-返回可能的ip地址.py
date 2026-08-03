"""
【字符串】给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
例子：输入 "25525511135"，输出 ["255.255.11.135", "255.255.111.35"]。
"""
def restore_ip_addresses(s):
    result = []
    n = len(s)
    # 第一段
    for i in range(1, 4):
        # 第二段
        for j in range(i + 1, i + 4):
            # 第三段
            for k in range(j + 1, j + 4):
                # 第四段
                a = s[:i]
                b = s[i:j]
                c = s[j:k]
                d = s[k:]
                # 判断长度
                if not (1 <= len(d) <= 3):
                    continue
                parts = [a, b, c, d]
                flag = True
                for part in parts:
                    # 前导0
                    if len(part) > 1 and part[0] == "0":
                        flag = False
                        break
                    # 范围
                    if int(part) > 255:
                        flag = False
                        break
                if flag:
                    result.append(".".join(parts))
    return result
s = "25525511135"
print(restore_ip_addresses(s))
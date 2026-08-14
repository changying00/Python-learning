import math 

# ceil 向上取整
print(math.ceil(3.1))  # 4
print(math.ceil(-3.1)) # -3

# floor 向下取整
print(math.floor(3.1))
print(math.floor(-3.1))

print(math.fabs(-3.2))
print(math.fabs(3.2))
print(math.fabs(-3))
print(math.fsum([1, 2, 3, 4, 5]))
# 求最大公约数
print(math.gcd(15, 27, 81))
# 获取一个数字的算术平方根 
print(math.sqrt(5),  math.isqrt(5))

print(float("nan") == float("nan"))
# 判断 一个数字 是否是 非数
print(math.isnan(float("nan"))) 

print(math.isinf(float("inf")),  math.isinf(float("-inf")))

print(math.isfinite(3), math.isfinite(float("nan")),  math.isfinite(float("inf")))

# math.sin(x)  :  求 正弦值 ,  x 代表 弧度
# math.cos(x)  :  求 余弦值 ,  x 代表 弧度
# math.tan(x)  :  求 正切值 ,  x 代表 弧度

# 弧度 和 度数 的计算公式 :   360度  = 2Π 弧度   --->   1度  =  Π/180 弧度  
print(math.pi)
# 计算 30度的 正弦值 
print(math.sin(210 * math.pi / 180)) 
# 计算 45度的 正切值 
# print(math.tan(45 * math.pi / 180))



def get_clock_locations(radius, center=(0, 0)):
    """
    获取 时钟 每个(12)刻度的 坐标位置
    """
    locations = []

    for k in range(12):
        # 计算 刻度 和 中心点的 夹角度数
        deg = k * 30 
        # 计算 x 刻度 对应的 相对于 中线点 x 坐标 
        x1 = math.sin(deg * math.pi / 180) * radius
        y1 = math.cos(deg * math.pi / 180) * radius

        x = round(x1 + center[0], 2)
        y = round(center[1] - y1, 2)


        locations.append((x, y))

    return locations 


print(get_clock_locations(10))




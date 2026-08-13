"""
【数学模块】编写一个函数 get_clock_location(center=(0, 0 ) , radius=100)
计算钟表中每一个整点刻度的坐标。 函数返回一个字典、键为 整点值 、 值为 长度为2的元组、代表 x, y 坐标
注意事项：
	1.  center 代表钟表外切最小正方形的  左上角的坐标位置
 	2.  radius 代表 圆的半径
"""
import math

#定义一个函数 get_clock_location
def get_clock_location(center=(0, 0 ) , radius=100):
       """获取钟表的整点刻度坐标"""
       result = {}
       #定义循环、遍历12次
       for x in range(12):
           #计算 x 刻度 和 12点方向夹角度数
            deg = x * 30
            loc_x = math.sin(deg * math.pi / 180) * radius  +  radius   + center[0]
            loc_y = radius - math.cos(deg * math.pi / 180) * radius +  center[1]
            if x == 0:
                result[12] =  (loc_x, loc_y)
            else:
                result[x] = (loc_x, loc_y)
       return result
if __name__ == '__main__':
     result = get_clock_location(center=(0, 0), radius=100)
     for item,value in result.items():
         print(item,value)
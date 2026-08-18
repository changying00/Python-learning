"""
IndexError : 索引异常

TypeError :  类型异常 

SyntaxError :  语法异常

NameError :  命名异常 

KeyError :  键异常

ValueError:  值异常

ZeroDivisionError : 除数不能为0异常

"""

# ls = [1, 2, 3]

# print(ls[3])
# print(ls * "3")
# 2_ab = 10
# print(ab)

#dct = {"name": "张三", "age": 20}

# print(dct["gender"])

# ls = [100, 200, 300, 400]

# ls.remove(600)
import hashlib


def test(string):

    s = hashlib.md5(string).hexdigest()
    
    print("over ..........................................................", s)


test("admin")
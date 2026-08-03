"""
index(sub,  start ? ,   end ?)  :   从指定区间 start ~ end 查找 第一次出现 sub子串的 索引位置、如果找不到，则报错 ！！！
rindex(sub, start ？,  end ?)  :   从指定区间 start ~ end 查找 最后一次出现的 sub字串的索引位置，找不到 报错！！！

find(sub,  start ?  , end ? ) :  从指定区间 start ~ end 查找 第一次出现 sub子串的 索引位置、找不到 返回  -1
rfind(sub, start? , end ?) :   从指定区间 start ~ end 查找 最后一次出现的 sub字串的索引位置，找不到 返回  -1

count(sub, start? , end ? )  :   从指定区间 start ~ end  获取 sub 子串 在区间内出现的次数
replace(old,  new ,  count=-1)  :   将 字符串中的 old 替换成 new,  默认-1替换全部， 如果指定 count , 可以设置替换次数


"""
string = 'dgx222hx'
#index使用
print(string.index('x'))
print(string.index('x',3))
#rindex
print(string.rindex('x'))

#find
print(string.find("S"))
#rfind
print(string.rfind("s"))
string = "DGXDGXDGX"
#count
print(string.count("DGX"))
#replace使用
print(string.replace("DGX","DX"))
print(string.replace("DGX","DX",1))
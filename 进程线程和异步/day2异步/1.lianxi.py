def flat(array):
    ls = []
    if array == []:
        return 
    for x in array:
        if type(x) != list:
            ls.append(x)
        else:
            flat(x) 
    return ls 
print(flat([1,2,[3,4,[5,6,[7,8]]]]))

a = 5
b = 7
a = a ^ b  #==> a = 5 ^ 7 = 2
b = a ^ b  #==> b = 2 ^ 7 = 5
a = a ^ b  #==> a = 2 ^ 5 = 7

a,b = b,a

print(a,b)
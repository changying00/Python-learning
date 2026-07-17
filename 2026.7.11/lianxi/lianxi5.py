"""

【分支】我家的狗5岁了，5岁的狗相当于人类多大呢？
其实，狗的前两年每一年相当于人类的10.5岁，之后每增加一年就增加四岁。 
那么5岁的狗相当于人类多少年龄呢？


"""
dog_age = int(input("请输入一个狗的年龄:"))
if 0<dog_age<=2:
  dog_age =  dog_age * 10.5
  print("狗的年龄为:",dog_age)
else:
  dog_age = 2 * 10.5 + (dog_age - 2)*4
  print("狗的年龄为:",dog_age)
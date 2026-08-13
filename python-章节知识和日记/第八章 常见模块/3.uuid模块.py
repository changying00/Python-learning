import uuid

x = uuid.uuid1()
x1 = uuid.uuid1()
print(x,x1)

x2 = uuid.uuid3(x,'徒步')
print(x2)

x3 = uuid.uuid4()

print(x3)

x4 =uuid.uuid5(x,'py2323')
print(x4.hex)
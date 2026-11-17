x=10
print("x=", "is with id: ", id(x), "and is of datatype: ", type(x))  #int
y=10
print(y, "is with id: ", id(y), "and is of datatype: ", type(y)) #int
print("Do they have the same id?", id(x) == id(y))
x=20
z=x
print(z, "is with id: ", id(z), "and is of datatype: ", type(z))  #int
print(x, "is with id: ", id(x), "and is of datatype: ", type(x))  #int
x=30
print(z, "is with id: ", id(z), "and is of datatype: ", type(z))  #int
print(x, "is with id: ", id(x), "and is of datatype: ", type(x))  #int


l1=[1,2,3]
print(l1, "is with id: ", id(l1), "and is of datatype: ", type(l1))  #list
l2=l1
print(l2, "is with id: ", id(l2), "and is of datatype: ", type(l2))  #list
print("Do they have the same id?", id(l1) == id(l2))
l1.append(4)
print(l1, "is with id: ", id(l1), "and is of datatype: ", type(l1))  #list
print(l2, "is with id: ", id(l2), "and is of datatype   : ", type(l2))  #list

t1=([1,2,3],4,5)
# t1=([5,6,7],8,9) + t1
t2=t1
print("id(",t1,")=",id(t1), "id(",t2,")=",id(t2))
t1[0].append(4)
print("id(",t1,")=",id(t1), "id(",t2,")=",id(t2))



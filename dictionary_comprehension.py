names=[("name","Vickey"),("occupation","Coder")]
# d={}
# for key,value in names:
#     d[key]=value
# print(d)
# print(type(d))

# shorter way of doing this
d={key: value for key,value in names}
print(d)  
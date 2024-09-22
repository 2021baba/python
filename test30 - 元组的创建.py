#第一种,使用()
t=('Python','hello',90)#()可省略
print(t)
print(type(t))
#只有一个元素,必须加
t1=(2,)
print(t1)
print(type(t1))
t2=(2)#不加为int型
print(t2)
print(type(t2))

#第二种,使用内置函数tuple()
t3=tuple(('Python','hello',90))
print(t3)
print(type(t3))

#空元组的创建
d=()
d2=tuple()
print(d)
print(d2)
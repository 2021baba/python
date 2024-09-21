#元组是python内置数据结构之一,是一个不可变序列
#字符串不可变(无增删改操作)
#列表,字典可以变(有增删改操作)
lst=[10,20,30]
print(id(lst))
lst.append(300)
print(id(lst))
#id没变,可变

#不可变
s='hello'
print(id(s))
s=s+'world'
print(id(s))
#id变,不可变

#元组
t=('Python','hello',90)
#列表
lst=['Python','hello',90]
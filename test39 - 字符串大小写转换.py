s = 'hello world'
a = s.upper()#转为大写
print(a,id(a))
print(s,id(s))
#转换后产生新的字符串

b = s.lower()#转为大写
print(b,id(b))

c = s.swapcase()#大写转为小写,小写转为大写
print(c,id(c))

d = s.capitalize()#把第一个转为大写,其他的转为小写
print(d,id(d))

e = s.title()#每个单词开头大写
print(e,id(e))

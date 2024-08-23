from turtle import TurtleGraphicsError

a = 10
print(type(a))
#变量的类型不需要显式声明，根据值来确定
#int可以自动扩容，无像long,short等类型
b = 0.5
print(type(b))
#float相对于C语言中的double
c = "hello"
print(type(c))#str字符串
#用引号连起字符叫字符串
#字符串中有引号用单双区分
#两个都有可以用"""和'''区分
print(len(c))

a1 = "hello"
a2 = "world"
print(a1 + a2)
#字符串的拼接,不可字符串和整型拼接

#布尔类型取值只有真假True和False大写
c1=True
c2=False
print(type(c1))
print(type(c2))
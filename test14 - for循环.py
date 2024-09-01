#可迭代对象(内部包含不同对象)

#打印1-10
for i in range (1,11):#range效果就是得到一个可迭代对象
    #range()前闭后开
    #range(a,b,c),c为步长默认为1
    print(i)

#打印2,4,6,8,10
for i in range(2,11,2):
    print(i)

#打印10-1
for i in range (10,0,-1):
    print(i)

#求1+2+3+4+5...+100
theSum = 0
for i in range (1,101):
    theSum += i
print(theSum)
#shift+F6批量更改变量名


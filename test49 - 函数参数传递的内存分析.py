def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1 = 100
    arg2.append(10)#增加一个10
    print('arg1', arg1)
    print('arg2', arg2)

n1 = 11
n2 = [22,33,44]
print(n1)
print(n2)
fun(n1,n2)#位置传参(函数定义的形参名称可以和实际参数不一样)
print(n1,n2)
"""在函数调用过程中,进行参数的传递
如果是不可变对象,在函数体的修改不会影响实参的值
如果是可变对象,在函数体的修改会影响实参的值"""
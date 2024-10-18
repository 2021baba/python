def fun(a,b):
    c=a+b#c就被称为局部变量,c为函数体内定义的变量,作用范围也是函数内部,a,b相当于局部变量
    print(c)

name='zyb'
print(name)
def fun2():
    print(name)

fun2()

def fun3():
    global age#函数内部定义的变量为局部变量,使用global声明的实际上是全局变量
    age=10
    print(age)
fun3()
print(age)

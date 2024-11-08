# 定义一个出现异常的函数
def func1():
    print('func1开始执行')
    num = 1/0
    print('func1结束执行')

# 定义一个无异常的函数,调用上面的函数
def func2():
    print('func2开始执行')
    func1()
    print('func2结束执行')

# 定义一个无异常的函数,调用上面的函数
def main():
    try:
        func2() #try,except不一定从真正出现异常的那一句话,只要函数之间有调用关系,可以在最高级的调用处捕获异常
    except Exception as e:
        print(f'出现异常了,异常信息是{e}')

main()

# 定义一个函数,接受其他函数输入
def test_func(compute):
    result = compute(1,2)
    print(f'计算结果为{result}')

# 通过lambda匿名函数形式,将匿名函数作为参数传入
test_func(lambda x , y : x + y)#只能写一行代码,只能单次使用



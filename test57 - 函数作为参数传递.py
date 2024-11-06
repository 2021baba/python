# 定义一个函数,接受另一个函数作为传入参数
def test_func(compute):
    result = compute(1,2)
    print(f'compute参数类型:{type(compute)}')
    print(f'计算结果为{result}')

# 定义一个函数,准备作为参数传入另一个函数
def compute(x,y):
    return x+y
test_func(compute)
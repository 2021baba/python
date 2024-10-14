def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in range(num):
        if num % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

lst = [10,20,30,40,50,60,70,80,90]
print(fun(lst))
'''
1.函数的返回值可以没有(函数执行后,不需要给调用处提供数据)return可以省略不写
2.函数的返回值,如果是一个,直接返回原值
2.函数的返回值,如果是多个,返回值为元组
'''
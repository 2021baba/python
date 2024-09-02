#while 条件:
#   循环体

#打印1-10
num = 1
while num<10:
    print(num)
    num += 1

#循环变量初始值
#循环判定条件
#循环变量的更新,不更新为死循环


#计算1 - 100的和
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print(sum)

#5的阶乘
result = 1
num = 1
while num <= 5:
    result *= num
    num += 1
print(result)

#1!+2!+3!+4!+5!

num = 1
sum = 0
while num <= 5:
    i = 1
    result = 1
    while i <= num :
        result *= i
        i += 1
    sum += result
    num += 1
print(sum)

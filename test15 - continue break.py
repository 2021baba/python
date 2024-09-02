#假设吃5个包子
for i in range(1,6):
    if i ==3:
        #发现第3个有虫
        continue#跳过一个循环,接着吃
    print(f"吃第{i}个包子")

for i in range(1,6):
    if i ==3:
        #发现第3个有虫
        break#跳出循环,不吃了
    print(f"吃第{i}个包子")

#给定若干数字,求平均值(不知道几个数字)
theSum = 0#表示加和结果
count = 0#表示几个数字
while True:
    num = input("请输入一组数字:(以;结束)")
    if num == ";":
        break
    num = float(num)
    theSum += num
    count += 1
print(f"平均值为{theSum/count}")

#每隔4年一次
#世纪闰年如果能被100整除,看是否能被400整除
year = int(input("请输入年份"))
if year % 100 == 0:
    if year % 400 == 0:#世纪闰年判断
        print("闰年")
    else:
        print("平年")
else:#普通闰年判断
    if year % 4 == 0:
        print("闰年")
    else:
        print("平年")

#压缩
if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0 :
    print("闰年")
else:
    print("平年")


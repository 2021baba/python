a = input("请输入一个数字a")
b = input("请输入一个数字b")
if a == "1":
    print("aaa")
    print("bbb")
#输入为1,输出aaa,bbb
#输入不为1,无输出

if b == "1":
    print("aaa")
print("bbb")
#输入为1,输出aaa,bbb
#输入不为1,输出bbb

if a == "1":
    if b == "1":
        print("aaa")#,两级缩进,两个条件都满足
    print("bbb")
print("ccc")
##输入都为1,输出aaa,bbb,ccc
##输入a为1,b不为1,输出bbb,ccc
##输入均不为1,输出ccc
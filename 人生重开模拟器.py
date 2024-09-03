import random

print("+----------------------------------------------------------+")
print("|                                                          |")
print("|                    花有重开日,人无再少年!                    |")
print("|                                                          |")
print("|                                                          |")
print("|                    欢迎来到人生重开模拟器                    |")
print("|                                                          |")
print("+----------------------------------------------------------+")

#设置初始属性(颜值,体质,家境,智力总和不超过20)

while True:#使用循环让玩家在输入错误时重新输入
    print("请输入初始属性")
    face=int(input("请输入颜值(1-10)"))
    strong=int(input("请输入体质(1-10)"))
    home=int(input("请输入家境(1-10)"))
    iq=int(input("请输入智力(1-10)"))

#通过条件语句,对用户输入的属性进行校验
#使用elif也可以
    if face < 1 or face > 10:
        print("颜值输入错误")
        continue
    if strong < 1 or strong > 10:
        print("体质输入错误")
        continue
    if home < 1 or home > 10:
        print("家境输入错误")
        continue
    if iq < 1 or iq > 10:
        print("智力输入错误")
        continue
    if face+iq+home+strong>20:
        print("总和大于20,输入错误")
        continue
    #如果上述条件没有触发,则输入正确,可跳出循环
    print("初始属性输入完毕!")
    print(f"颜值为{face},体质为{strong},智力为{iq},家境为{home}")
    break

#生成角色性别
#使用 random.randint(begin,end),能生成范围内的随机数
point=random.randint(1,6)
if point%2==1:
    gender = "boy"
    print("你是个男孩")
if point%2==0:
    gender = "girl"
    print("你是个女孩")





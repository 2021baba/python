import random
import sys
from datetime import time
import time

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

#生成角色出生点
#家境 + 随机数



#1-3 第四档 倒扣
point = random.randint(1,3)
if home == 10:#家境 10 第一档 加成
    print("你出生在帝宫,父母是高官政要")
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:#7-9 第二档 加成
    if point == 1:
        print("你出生在大城市,父母是公务员")
        face += 2
    elif point == 2:
        print("你出生在大城市,父母是企业家")
        home += 2
    else:
        print("你出生在大城市,父母是大学教授")
        iq += 2

elif 4 <= home <= 6:#4-6 第三档 少量加成
    if point == 1:
        print("你出生在三线城市,父母是医生")
        strong += 1
    elif point == 2:
        print("你出生在小镇,父母是老师")
        iq += 1
    else:
        print("你出生在三线城市,父母是个体户")
        home += 1



else:#1-3 第四档 倒扣
    if point == 1:
        print("你出生在农村,父母是农民")
        strong += 1
        face -= 2
    elif point == 2:
        print("你出生在农村,父母是无业游民")
        home -= 1
    else:
        print("你出生在小镇,父母感情不和")
        strong -= 1
print(f"颜值:{face},家境:{home},体质:{strong},智力:{iq}")

#幼年(1-10)   可塑性强
age = 1
for age in range(1,11):
    info = f"你今年{age}岁"
    point = random.randint(1,3)
    #编写事件
    #性别触发
    if gender == "girl" and home <= 3 and point == 1:
        info += "你的父母重男轻女,你被遗弃了"
        print(info)
        print("游戏结束")
        sys.exit(0)#sys为system缩写
    # 体质触发
    elif strong <6 and point <= 3:
        info += "你生了一场病"
        if home >=5:
            info +="你在父母的照料下康复了"
            strong += 1
            home -= 1
        else:
            info += "父母很忙没时间管你"
            strong -= 1
    # 颜值触发
    elif face <=4 and age >= 7:
        info +="你长得太丑了"
        if iq>5:
            info+="你决定用学习填充自己"
            iq += 1
        else:
            if gender == "boy":
                info +="你和别人打架"
                strong += 1
                iq -= 1
            else:
                info += "你总被欺负"
                strong -= 1
    # 智商触发
    elif iq<5:
        info += "你看起来傻傻的"
        if home >= 8 and age >= 6:
            info += "你父母把你送到更好的学校学习"
            iq +=1
        elif 4 <= home <= 7:
            if gender == "boy":
                info += "你父母鼓励你多运动,争取成为运动员"
                strong +=1
            else:
                info += "你父母鼓励你多打扮自己"
                face +=1
        else:
            info +="你的父母因此经常吵架"
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -=1
            else:
                pass

    else:
        info+="你健康成长"
        if point == 1:
            strong += 1
            info += "你看起来跟结实了"
        elif point == 2:
            face += 1
            info += "你看起来跟好看了"
        else:
            pass
    print(info)
    print(f"颜值:{face},家境:{home},体质:{strong},智力:{iq}")
    print("--------------------------------------------------------")
    time.sleep(1)#暂停操作





    #



#青年(11-20)   求学
#壮年(21-50)  平稳
#老年(50以上)   颜值体质智力退化













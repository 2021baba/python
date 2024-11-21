# 构造方法名称:__init__
class Student:
    # 构造方法自动执行,注意有self
    def __init__(self, name, age,tel):
        self.name = name             #记录姓名
        self.age = age              #记录年龄
        self.tel = tel              #记录电话
        print('证明自动执行')

stu = Student('zyb',18,15062241087)

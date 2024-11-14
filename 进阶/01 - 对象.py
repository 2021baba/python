# 设计一个类(类比生活中:设计一张登记表)
class Student:
    name = None             #记录姓名
    gender = None           #记录性别
    nationality = None      #记录国籍
    native_place = None   #记录籍贯
    age = None              #记录年龄

# 创建一个对象(类比生活中:打印一张登记表)
stu_1 = Student()

# 对象属性进行赋值(类比生活中:填写表单)
stu_1.name = 'zyb'
stu_1.gender = 'male'
stu_1.age = 18
stu_1.nationality = '中国'
stu_1.native_place = '江苏'

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1)

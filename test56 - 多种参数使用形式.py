def user_info(name,age,gender):
    print(f'name is {name} , age is {age} , gender is {gender} ')


# 位置传参
user_info('小明',18,'男')


# 关键字传参
user_info(name='小明',age=18,gender='男')
user_info(age=18,gender='男',name='小明')
# 位置无所谓


# 缺省参数
def user_info(name,age,gender='男'):
    print(f'name is {name} , age is {age} , gender is {gender} ')

user_info('小明',18)
# 定义的时候可以设置默认值,默认值必须在最后


# 不定长参数 - 位置不定长(*号)
#长度不受限制
def user_info(*args):
    print(f'args is {args} ')

user_info(1,2,3,4,5,'小明')


# 不定长参数 - 关键字不定长(**号)
def user_info(**kwargs):
    print(f'kwargs is {kwargs} ')

user_info(name='小明',age=18,gender='男')
#只能传入键值对的形式的参数
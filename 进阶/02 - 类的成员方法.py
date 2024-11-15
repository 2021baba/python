# 定义一个带有成员方法的类
class Student:
    name = None

    def sayHello(self):
        print(f'大家好,我是{self.name}')

    def sayHello2(self,msg):
        print(f'大家好,我是{self.name},{msg}')
    #访问成员变量前面self.变量名

student1 = Student()
student1.name = '周杰伦'
student1.sayHello()
student1.sayHello2('哎哟不错呦')

student2 = Student()
student2.name = '林俊杰'
student2.sayHello()
student2.sayHello2('小伙子,我看好你')
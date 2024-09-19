#1.键不可以重复,值可以重复
d = {'name':'张三','name':'李四'}
print(d)
#键不可以重复
d = {'name':'张三','nikename':'张三'}
print(d)
#值可以重复

#2.字典元素是无序的
#列表是有序的
lst=[10,20,30]
lst.insert(1,100)
print(lst)

#3.键是不可变的对象
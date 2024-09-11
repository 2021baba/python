#添加
#append向列表末尾添加一个元素,不更改列表对象(id)
lst=[10,20,30]
print(lst,id(lst))
lst.append(40)
print(lst,id(lst))

#extend向列表末尾添加至少一个元素,可一次性添加多个元素
lst2=['hello','world']
lst.extend(lst2)
print(lst)

#insert在任意位置添加一个元素
lst.insert(1,90)
#在索引为1的位置上添加90
print(lst)

#切片在任意位置添加至少一个元素,可一次性添加多个元素
lst3=['hello','world']
lst[1:]=lst3#将索引为1的后面元素改为lst3
print(lst)
lst[1:1]=lst3#将索引为1,2之间元素改为lst3
print(lst)

#删除
#remove删除一个元素
lst=[10,20,30,40,50,60,70,80,90]
print(lst)
lst.remove(30)#移除第一个30
print(lst)

#pop删除指定索引上的元素
lst.pop(1)#不写参数删除最后一个元素
print(lst)

#切片删除至少一个元素
lst=lst[1:3]
print(lst)
lst=[10,20,30,40,50,60,70,80,90]
lst[1:3]=[]#用空列表删除
print(lst)

#cleer清空列表
lst.clear()
print(lst)

#del删除列表
del lst

#修改列表
#一次修改一个值
lst=[10,20,30,40,50,60,70,80,90]
lst[2]=100
print(lst)

#使用切片一次修改多个值
lst[1:3]=[100,200,300]
print(lst)


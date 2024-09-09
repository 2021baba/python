#获取单个元素
lst=["hello","world","hello",98]
print(lst[2])#获取索引为2的元素
print(lst[-1])#获取索引为-1的元素

#获取多个元素,切片
lst2=[10,20,30,40,50,60,70,80,90]
print(id(lst2))
lst3=(lst2[1:6:1])
#切出列表,[开始:结束:步长],不包括结束
#步长为正数
print(lst3)#默认步长为1
lst4=(lst2[:6:1])#默认开始是0
print(lst4)
lst5=(lst2[1::1])#默认结束是最后一个
print(lst5)

#步长为负数
lst6=(lst2[::-1])
print(lst6)#第一个元素是列表最后一个,最后一个是列表第一个


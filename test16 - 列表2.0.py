#创建列表第一种方式,使用[]
lst = ["hello", "world" ,98,"hello"]
#可以重复数据
#创建列表第二种方式,使用内置函数list()
lst2=list(["hello", "world" ,98])

#列表特点
#有序排序
print(lst[0],lst[-3])
#索引从0开始计算,从后往前采用负数索引-1是最后一个

#任意类型
print(lst.index("hello"))
#index获取元素索引,重复只获取第一个
print(lst.index("hello",1,4))
#index在[1,4)获取元素索引,索引从1开始

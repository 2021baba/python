#使用sort排列,不产生新列表
lst=[20,40,10,50,90,1]
print("排序前",lst,id(lst))
#sort方法默认升序排列
lst.sort()#()中默认reverse=False
print("排序后",lst,id(lst))
#sort排列未改变列表id

#sort(reverse=True)降序排列
lst.sort(reverse=True)
print(lst)

#使用sorted()进行排列,产生新列表
lst=[20,40,10,50,90,1]
#开始排序
new_lst = sorted(lst)
print(new_lst)
#指定关键字参数,实现降序排列
new_lst = sorted(lst, reverse=True)
print(new_lst)

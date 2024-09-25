#判断 in,not in
s={10,20,30,40,50,60,70,80,90}
print(10 in s)
print(200 in s)
print(200 not in s)
print(10 not in s)

#新增
s={10,20,30,40,50,60,70,80,90}
s.add(80)#加一个
print(s)

s.update({200,400,300})#至少加一个
print(s)
s.update([2000,3000,4000])
print(s)

#删除
s.remove(10)#删除元素必须存在,否则keyerroy
print(s)
s.discard(1000)#删除元素不是必须存在
print(s)
s.pop()#删除一个随机元素,不能指定参数
print(s)
s.clear()#清空集合
print(s)


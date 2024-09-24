s = {1,1,2,1,3,1,23,1,2}
print(s)
#元素不重复,重复的会被去掉

s1 = set(range(6))
print(s1)

s2 = set([1,2,3,4,5,6])
print(s2)

s3=set((1,231,32,12))
print(s3)
#输出{32, 1, 12, 231}集合元素无序

s4=set('python')
print(s4)
#集合元素无序,输出{'y', 'n', 'p', 'o', 'h', 't'}

#空集合
s6 = set()
print(s6)
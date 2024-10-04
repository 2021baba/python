s = 'hello world'
lst = s.split()
print(lst)

#split默认从左侧分割
s1 = 'hello|world|Python'
print(s1.split(sep='|'))#sep=来指定分割符
print(s1.split(sep='|', maxsplit=1))#maxsplit指定最大分割段数

#rsplit默认从右侧分割
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))


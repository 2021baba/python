s = 'hello world'
#居中对齐
print(s.center(20,'*'))
print(s.center(20))#默认填充为空格
#左对齐
print(s.ljust(20,'*'))
#右对齐
print(s.rjust(20,'*'))
#右对齐,使用0进行填充
print(s.zfill(20))
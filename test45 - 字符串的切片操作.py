s = 'hello world'
'''完整写法s[start:stop:step]'''
s1 = s[0:5]#不写起始位置,默认从0
print(s1)

s2 = s[6:]#不写最后位置,默认到字符串结束
print(s2)

s3 = '!'
s4 = s1 + s3 + s2
print(s4)
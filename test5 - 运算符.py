#算术运算符  +-*/%
#(先乘除,再加减,0不能作为除数)有小数会保留

#关系运算符  > < >= <= ==
a=10
b=20
c=30
print(a>b)
print(a<b)
print(a==b)
#逻辑运算符
# and 并且
# or 或者
# not 逻辑取反
print(a<b and b<c)
print(a<c and c<b)

print(a<c or c<b)
print(a<b or b<c)
print(a<c or c<b)

print(not b<c)
print(not c<b)
#赋值运算符

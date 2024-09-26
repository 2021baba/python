#集合是否相等
s={10,20,30}
s2={20,30,10}
print(s==s2)
print(s!=s2)

#集合子集
s1={20,30,10,40,50,60}
s2={20,30,10,40}
s3={20,30,10}
print(s2.issubset(s1))
print(s3.issubset(s1))

#集合超集(子集反过来)
print(s2.issuperset(s1))
print(s3.issuperset(s1))

#是否有交集
print(s2.isdisjoint(s3))


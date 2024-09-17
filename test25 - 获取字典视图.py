scorss={'1':100,'2':98,'3':20}
#keys()获取所有的键
keys = scorss.keys()
print(keys)
print(type(keys))
print(list(keys))#将所有键组成的视图转成列表

#values()获取所有的值
values = scorss.values()
print(values)
print(type(values))
print(list(values))

#items()获取所有的键值对
items = scorss.items()
print(items)
print(type(items))
print(list(items))
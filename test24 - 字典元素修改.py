#键对值在不在的判断
scorss={'1':100,'2':98,'3':20}
print('1' in scorss)
print('2' not in scorss)

#删除指定键对值
del scorss['1']
print(scorss)
scorss.clear()#清空字典元素
print(scorss)

#增加元素
scorss['4']=99
print(scorss)

#修改元素
scorss['4']=999
print(scorss)



scorss={'1':100,'2':98,'3':20}
#[]
print(scorss['1'])
#值不存在时报错

#.get()
print(scorss.get('1'))
print(scorss.get('20'))
#值不存在时不报错,输出None
print(scorss.get('30',99))
#99为不存在时输出的默认值

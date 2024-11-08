# 导入Python内置的time模块,Ctrl点击time可跳转到源码
# import time
# print('你好')
# time.sleep(2)
# .表示sleep函数属于time模块,通过. 就可以使用模块内部全部功能(类,函数,变量)
# print('你好')

# 使用from导入time的sleep功能
# from time import sleep
# print('你好')
# sleep(5)
# print('你好')

# 使用 * 导入time所有模块
from time import *          # *表示全部的意思
print('你好')
sleep(5)
print('你好')

# 所有as给特定功能加上别名
import time as t
print('你好')
t.sleep(5)
print('你好')

from time import sleep as sl
print('你好')
sl(3)
print('你好')

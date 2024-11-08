import time
# w模式打开文件,不存在的文件会自动创建,存在的文件会被清空
f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\test1.txt','w',encoding='utf8')

# write写入
f.write('hello world')              #程序运行时内容写入内存中,结束才写入硬盘

# flush刷新
f.flush()                           #将内存中数据写入硬盘中

# 文件关闭
f.close()                           #closh内置flush

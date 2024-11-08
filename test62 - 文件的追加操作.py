# a模式打开文件,不存在的文件会自动创建,存在的文件会在最后追加写入文件,不会清空
f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\test2.txt','a',encoding='utf8')
# write写入
f.write('test2')
# flush刷新
f.flush()
#close关闭
f.close()

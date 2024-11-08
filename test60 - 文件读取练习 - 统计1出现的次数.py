# 打开文件,以读取模式打开
f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\test.txt','r',encoding='utf8')
# 方式一,读取全部内容,通过count方法统计1数量
# content = f.read()
# count = content.count('1')
# print(count)

# 方式二,一行一行读取
count = 0  #使用count变量来累积1出现的次数

for i in f:
    words = i.strip().split(' ')#去除/n,开头结尾的空格,按' '分隔
    for word in words:  # 判断单词并累加
        if word == '1':
            count = count + 1
print(count)

f.close()



# 打开文件 - open()
f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\test.txt','r',encoding='utf8')
print(type(f))
# 读取文件 - read()
print(f'读取10个字节的结果{f.read(10)}')
print(f'读取全部内容的结果{f.read()}')
# 第二次读取会读取第一次读取从剩下的开始

# 读取文件 - readlines()
lines =f.readlines()#读取文件的全部行,封装到列表中
print(f'lines内容为{lines}')

# 读取文件 - readline()
line1 =f.readline()
line2 =f.readline()
line3 =f.readline()
print(line1)
print(line2)
print(line3)

# for循环读取文件行
for line in f:
    print(line)

# 文件的关闭
f.close()

# with open语法操作文件
with open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\test.txt','r',encoding='utf8') as f:
    for line in f:
        print(line)
# 会自动关闭文件
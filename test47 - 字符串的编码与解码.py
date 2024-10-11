s = '天涯共此时'
#编码
print(s.encode(encoding='GBK'))#一个中文占两个字节
print(s.encode(encoding='UTF-8'))#一个中文占三个字节

#解码
#byte代表二进制数据
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
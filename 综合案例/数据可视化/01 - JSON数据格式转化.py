import json

# 准备列表,列表中每个元素都是字典,将其转化为JSON
data = [{'name':'小明','age':18},{'name':'小王','age':16},{'name':'小黄','age':20}]
json_data = json.dumps(data,ensure_ascii=False)#使用ensure_ascii=False(不使用ascii码)来使中文正常显示
print(json_data)
print(type(json_data))

# 准备字典,将字典转化为JSON
data2 = {'name':'小fang','age':14}
json_data2 = json.dumps(data2,ensure_ascii=False)
print(json_data2)
print(type(json_data2))

# 将JSON字符串转换为Python数据类型(列表)  [{K:v,K:v},{K:v,K:v}]
s = '[{"name":"小明","age":18},{"name":"小王","age":16},{"name":"小黄","age":20}]'
l = json.loads(s)
print(l)
print(type(l))

# 将JSON字符串转换为Python数据类型(字典)  {K:v,K:v}
s = '{"name":"小明","age":18}'
d = json.loads(s)
print(d)
print(type(d))
s = 'hello world'
#isidentifier判断是否是合法字符串
print(s.isidentifier())#False
print('hello'.isidentifier())#True
print('张三'.isidentifier())#True

#isspace判断字符串是否有空白字符串组成(回车,换行,水平制表符)
print('\t'.isspace())

#isalpha判断字符串是否全部由字母,汉字组成
print('abc'.isalpha())
print('张三'.isalpha())

#isdecimal判断字符串是否由十进制数组成(汉字数字,罗马数字不算)
print('9'.isdecimal())
print('123四'.isdecimal())#False

#isnumeric判断字符串是否由数字组成(汉字数字,罗马数字算)
print('9'.isnumeric())
print('123四'.isnumeric())#True

#isalnum判断字符串是否由数字字母组成
print('abc1'.isalnum())




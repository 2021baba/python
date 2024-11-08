# 基本捕获语法
from logging import exception

try:
    f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill2.txt','r',encoding='utf-8')
except:         #出现异常后不报错,所以异常被except捕获,执行以下程序
    print('出现异常了,我将open模式改为''w''去打开')
    f = open('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill2.txt','w',encoding='utf-8')

# 捕获指定异常
try:
    print(name)
except NameError as e:      #只捕获变量未定义的异常
    print('出现变量未定义的异常')

# 捕获多个异常
try:
    print(name)
    1 / 0
except (NameError,ZeroDivisionError) as e:      #捕获多个异常
    print('出现变量未定义 或者除以0 的异常')

# 捕获全部异常
try:
    print(name)
    1 / 0
# except:      #捕获全部异常
#     print('出现异常')

except Exception as e:      #两种都是捕获全部异常
    print('出现异常')
else:                       #else无异常时执行以下代码
    print('无异常')
finally:                    #finally有没有异常都执行以下代码
    f.close()
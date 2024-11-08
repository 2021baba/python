# 导入自定义模块
from importlib import import_module

import my_modulel1
#my_modulel为自定义模块,项目中为一个python文件
my_modulel1.test(1,2)

# 导入不同模块的同名功能
from my_modulel1 import test
from my_modulel2 import test
# 不同模块的同名功能,后导入的会覆盖前导入的
test(1,2)

# __main__变量
# 当自定义模块中有测试运行语句时,添加if __name__ =='__main__':可避免模块调用时运行测试语句
from my_modulel1 import test
test(1,2)

#__all__变量
# 当设置 __all__ = [''] 时,import * 只能导入[]内的函数
from my_modulel1 import *
test(1,2)
# test1(1,2)无法使用
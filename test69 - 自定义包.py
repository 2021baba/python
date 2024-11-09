# 创建一个包
# 包文件夹中一定包含__init__.py文件

# 导入自定义的包中的模块,并使用
# 三种写法
# import my_package.my_modulel1
# import my_package.my_modulel2
# my_package.my_modulel1.info_print1()
# my_package.my_modulel2.info_print2()
#
# from my_package import my_modulel1
# from my_package import my_modulel2
# my_modulel1.info_print1()
# my_modulel2.info_print2()

# from my_package.my_modulel1 import info_print1
# from my_package.my_modulel2 import info_print2
# info_print1()
# info_print2()

# __all__变量,控制import *
# 在__init__.py文件中写__all__ = ['']可控制import *导入的内容
from my_package import *
my_modulel1.info_print1()
# my_modulel2.info_print2() #无法使用
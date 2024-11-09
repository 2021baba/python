import my_utils.file_util
import my_utils.str_util

print(my_utils.str_util.str_reverse('12123'))
print(my_utils.str_util.substr('12321123',1,4))

my_utils.file_util.print_file_info('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt')
my_utils.file_util.append_to_file('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt','data')

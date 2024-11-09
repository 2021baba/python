def print_file_info(file_name):
    '''
    读取文件内容
    :param file_name:文件路径
    :return: None
    '''
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
        content = f.read()
        print(f'文件内容为{content}')
    except Exception as e:
        print(f'出现异常,异常为{e}')
    finally:
        if f:       #如果变量为None,则无须关闭文件,则不会报错
            f.close()

def append_to_file(file_name,data):
    '''
    在文件后添加内容
    :param file_name:文件路径
    :param data: 添加的内容
    :return: None
    '''
    f = None
    try:
        f = open(file_name, 'a', encoding='utf-8')
        f.write(data)
        f.write('\n')
    except Exception as e:
        print(f'出现异常,异常为{e}')
    finally:
        if f:
            f.close()



if __name__ == '__main__':
    print_file_info('hello.txt')
    append_to_file('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt','data')
    print_file_info('C:\\Users\\29174\\Desktop\\Code\\python\\hello\\文件\\bill.txt')

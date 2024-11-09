def str_reverse(s):
    '''
    功能是将字符串反转
    :param s: 将被反转的字符串
    :return: 反转后的字符串
    '''
    return s[::-1]

def substr(x,y,z):
    '''
    功能是完成字符串的切片
    :param x: 即将被切片的字符串
    :param y: 切片开始的下标
    :param z: 切片结束的下标
    :return: 切片后的字符串
    '''
    return x[y:z:1]

if __name__ == '__main__':
    print(str_reverse("123123231"))
    print(substr('123123',1,3))
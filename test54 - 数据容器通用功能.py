my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = 'abcdefg'
my_set = {1,2,3,4,5}
my_dict = {'key1':1,'key2':2,'key3':3,'key4':4,'key5':5}

# len元素个数
print(f'列表元素个数有: {len(my_list)}')
print(f'元组元素个数有: {len(my_tuple)}')
print(f'字符串元素个数有: {len(my_str)}')
print(f'集合元素个数有: {len(my_set)}')
print(f'字典元素个数有: {len(my_dict)}')

# max最大元素
print(f'列表最大元素为: {max(my_list)}')
print(f'元组最大元素为: {max(my_tuple)}')
print(f'字符串最大元素为: {max(my_str)}')
print(f'集合最大元素为: {max(my_set)}')
print(f'字典最大元素为: {max(my_dict)}')

# min最小元素
print(f'列表最小元素为: {min(my_list)}')
print(f'元组最小元素为: {min(my_tuple)}')
print(f'字符串最小元素为: {min(my_str)}')
print(f'集合最小元素为: {min(my_set)}')
print(f'字典最小元素为: {min(my_dict)}')

# 类型转换

# 转列表
print(f'列表转列表的结果是: {list(my_list)}')
print(f'元组转列表的结果是: {list(my_tuple)}')
print(f'字符串转列表的结果是: {list(my_str)}')
print(f'集合转列表的结果是: {list(my_set)}')
print(f'字典转列表的结果是: {list(my_dict)}')

# 转元组
print(f'列表转元组的结果是: {tuple(my_list)}')
print(f'元组转元组的结果是: {tuple(my_tuple)}')
print(f'字符串转元组的结果是: {tuple(my_str)}')
print(f'集合转元组的结果是: {tuple(my_set)}')
print(f'字典转元组的结果是: {tuple(my_dict)}')

# 转字符串
print(f'列表转字符串的结果是: {str(my_list)}')
print(f'元组转字符串的结果是: {str(my_tuple)}')
print(f'字符串转字符串的结果是: {str(my_str)}')
print(f'集合转字符串的结果是: {str(my_set)}')
print(f'字典转字符串的结果是: {str(my_dict)}')

#转集合
print(f'列表转集合的结果是: {set(my_list)}')
print(f'元组转集合的结果是: {set(my_tuple)}')
print(f'字符串转集合的结果是: {set(my_str)}')
print(f'集合转集合的结果是: {set(my_set)}')
print(f'字典转集合的结果是: {set(my_dict)}')

#sorted排序
print(f'列表sorted排序: {sorted(my_list)}')
print(f'元组sorted排序: {sorted(my_tuple)}')
print(f'字符串sorted排序: {sorted(my_str)}')
print(f'集合sorted排序: {sorted(my_set)}')
print(f'字典sorted排序: {sorted(my_dict)}')

# 从大到小排序
print(f'列表sorted反向排序: {sorted(my_list,reverse = True)}')
print(f'元组sorted反向排序: {sorted(my_tuple,reverse = True )}')
print(f'字符串sorted反向排序: {sorted(my_str,reverse = True)}')
print(f'集合sorted反向排序: {sorted(my_set,reverse = True)}')
print(f'字典sorted反向排序: {sorted(my_dict,reverse = True)}')

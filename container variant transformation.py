# 容器类型数据转换


# list tuple set dict

# list
'''
    字符串 转换为列表 会把字符串中的每一个字符当作列表的元素
    数字类型是 肺容器类型， 不能转换为元素
    集合 可以转换为 list类型
    元组 可以转换为 list类型
    字典 可以转换为 list类型，只保留了字典中的键
'''

# tuple
'''
数字类型 非容器类型， 不能转换为元组
其他容器类型转换和列表一样

'''
# set
'''
数字类型 非容器类型， 不能转换为 集合
字符串， 列表，元组 可以转换为 集合 结果为无序
字典 转换为 集合，只保留了键 key
'''

# dict 字典
'''
数字类型 非容器类型， 不能转换为 字典 
字符串不能直接转换为 字典

列表可以转换为字典，要求是一个二级列表并且每个二级元素只能为两个值  # n = [[1,2],['a', 'b], ['11', 11]]
元组可以转换为字典，要求是一个二级元组并且每个二级元素只能为两个值
集合中的的两个元素是元组可实现转换

'''
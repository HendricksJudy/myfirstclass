# 元组类型tuple

'''
+ 在定义多个数据时可以选择list，还可以使用元组类型来定义
+ 元组和list1相似，都用于储存多个数据使用
+ list用中括号进行定义，元组使用小括号进行定义

'''
# tuple
var = (1, 2, 3, 'a', 'b' )  # <class 'tuple'>
# print(var, type(var))
# print(var[3])

# 元组定义时只有一个元素，那么需要加逗号，不然会变成其他的其他类型
# var = (123, )  # <class 'tuple'>
# print(var, type(var))

# 元组的其他定义方式
var = 1, 2, 3  # <class 'tuple'>

# 列表与元组的区别
'''
+ 列表使用中括号定义
+ 元组使用小括号定义
+ 列表中的值可以改表
+ 元组中的值不可改变
'''

# 定义列表
varl = [1, 2,2]
# 通过下标进行元素值的修改
varl[2] = 33
# print(varl)

# 定义元组
vart = (1, 2, 3)
vart[2] = 33
print(vart)  # 错误：元组的值不可被改变  TypeError: 'tuple' object does not support item assignment
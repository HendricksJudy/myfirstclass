# coding: utf-8

# 变量定义的方式

# 定义变量时，要注意遵守变量命名规范

# 1. 直接单个赋值
# a = 10
# b = 20


# 2. 直接连续赋值

# a, b = 30, 40

# 交换变量的数据
a = 10
b = 20

'''
普通方式，完成变量数据的交换
1. 定义c变量 接收 a变量值， 此时 c变量即为 10
2. 把b变量的值，赋值给a ， 此时a变量即为 20
3. 把c变量的值，赋值给b ， 此时 b变量即为 10
'''
# c = a
# a = b
# b = c

'''
利用python定义变量的语法实现 变量的数据交换
'''
# a, b = b, a

print(a, b)


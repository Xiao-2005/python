# 1. 语法斩首战（72小时）
# - 暴力对比C++差异表：列表推导式替代for循环、动态类型暗黑机制、鸭子类型偷袭技巧
# - 用vim/VS Code写100行烂代码，故意触发TypeError/IndentationError喂给ChatGPT鞭尸
# - 手撕numpy实现矩阵乘法，必须比C++向量化版本快3倍才算过关


# for 循环
#先创建两个变量
# a=[1,2,3,4]
# b={"key1":"value1","key2":"value2"}
# 第一种，常规写法
# for x in range(123):
#
# for x in range(len(a)):
#
# for x in range(14,125):  # 实际为14-124

# 第二种，遍历数组或字典
# for x in(a,b):
# 第三种
# list_data=[x for x in range(123)]
# 等同于
# list_data=[]
# for x in range(123):
#     list_data.append(x)
#
# list_data=[x for x in a]
# 等同于
# list_data=[]
# for x in a:
#     list_data.append(x)
#
# list_data=[x for x in range(256) if x%2!=0]
# 等同于
# list_data=[]
# for x in range(256):
#     if x%2!=0:
#         list_data.append(x)

# while 语句，除了缩进和冒号，无区别。python里面没有do while

#   函数
# def 函数名(实参):
#     code

# 字符串拼接，比较，函数赋值
# 拼接
# a="abc"
# b="def"
#
# a=a+b
#
# 比较
# a == b
# a is b
# id(a) == id(b)#比较内存地址
#
# 函数赋值
# 输出可以显示拼接结果但是原来字母并未改变，必须使用语句赋值



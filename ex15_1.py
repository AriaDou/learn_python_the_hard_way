# -*- coding: utf-8 -*-
# 导入sys模块
from sys import argv

# 读取argv列表中的参数
script, filename = argv

# 打开filename文件
txt = open(filename)

# 打印filename字符串
print "Here's your file %r:" % filename
# 打印filename文件中的内容
print txt.read()

# 打印文字
print "Type the filename again:"
# 输入文件名赋给变量file_agian
file_again = raw_input(">")

# 打开file_again文件
txt_again = open(file_again)

# 打印file_again文件中的内容
print txt_again.read()

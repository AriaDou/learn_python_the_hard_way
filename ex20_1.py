# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    #输出整个文件
    print f.read()

def rewind(f):
    #移动文件读取指针到文件开头
    f.seek(0)

#输出该行行号，并读取这一行
def print_a_line(line_count, f):
    print line_count, f.readline()

#打开文件
current_file = open(input_file)

print "First let's print the whole file:\n"
#输出整个文件
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#回退读取指针到文件开头
rewind(current_file)

print "Let's print three lines:"

current_line = 1
#输出第一行内容
print_a_line(current_line, current_file)

current_line = current_line + 1
#输出第二行内容
print_a_line(current_line, current_file)

current_line = current_line + 1
#输出第三行内容
print_a_line(current_line, current_file)

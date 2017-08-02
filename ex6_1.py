# -*- coding: utf-8 -*-
# 把10以整数的形式插入
x = "There are %d types of people." % 10
# 赋值binary
binary = "binary"
do_not = "don't"
# 把binary, do_not两个变量以字符串的形式插入
y = "Those who know %s and those who %s." % (binary, do_not)

# 输出x
print x
# 输出y
print y

# 把x变量以原始数据的形式插入
print "I said: %r." % x
# 把y变量以字符串的形式插入
print "I also said: '%s'." % y

# 赋值hilarious
hilarious = False

#赋值joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#把hilarious变量以原始数据的形式插入
print joke_evaluation % hilarious

# 赋值w
w = "This is the left side of... "
# 赋值e
e = "a string with a right side."

# 字符串拼接
print w + e

#有6处“把一个字符串放进另一个字符串” 的情况

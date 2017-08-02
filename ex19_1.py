# -*- coding: utf-8 -*-
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# 将20传递给cheese_count参数，将30传递给boxes_of_crackers参数
# 运行cheese_and_crackers函数
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# 将amount_of_cheese的值传递给cheese_count参数
# 将amount_of_crackers的值传递给boxes_of_crackers参数
# 运行cheese_and_crackers函数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# 将10加20的和传递给cheese_count参数，将5加6的和传递给boxes_of_crackers参数
# 运行cheese_and_crackers函数
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# 将amount_of_cheese加100的和传递给cheese_count参数
# 将amount_of_crackers加1000的和传递给boxes_of_crackers参数
# 运行cheese_and_crackers函数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

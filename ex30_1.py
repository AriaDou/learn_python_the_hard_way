# -*- coding: utf-8 -*-
people = 20
cars = 40
buses = 15

# 如果小汽车比人多，输出“我们该坐小汽车”
if cars > people:
    print "We should take the cars."
# 不满足上述条件的同时，如果小汽车比人少，输出“我们不应该坐小汽车”
elif cars < people:
    print "We should not take the cars."
# 除此之外，输出“我们无法决定”
else:
    print "We can't decide."

# 如果巴士比小轿车多，输出“有太多巴士了”
if buses > cars:
    print "That's too many buses."
# 不满足上述条件的同时，如果巴士比小汽车少，输出“也许我们可以坐巴士”
elif buses < cars:
    print "Maybe we could take the buses."
# 除此之外，输出“我们仍然无法决定” 
else:
    print "We still can't decide."


if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

if cars > people and buses < cars:
    print "cars too much!"

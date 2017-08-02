# -*- coding: utf-8 -*-
people = 20
cats = 30
dogs = 15

# if:当满足条件的时候，执行if之后的代码块，直至代码块结束。
# 如果if的下一行不缩减，会报错，因为“：”的下一行是一定要缩进的
if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if True and False:
    print "True and False: True."
else:
    print "True and False: False"

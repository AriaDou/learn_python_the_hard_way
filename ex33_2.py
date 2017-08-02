# -*- coding: utf-8 -*-
def setNum(end, delta):
    i = 0
    numbers = []
    while i < end:
        print "At the top i is %d" % i
        numbers.append(i)

        i += delta
        print "Numbers now:", numbers
        print "At the bottom i is %d" % i
    return numbers

numbers = setNum(6, 2)

print "The numbers:"

for num in numbers:
    print num

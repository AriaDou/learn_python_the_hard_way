# -*- coding: utf-8 -*-
def setNum(end):
    i = 0
    numbers = []
    for i in range(0, end):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now:", numbers
        print "At the bottom i is %d" % (i + 1)
    return numbers

numbers = setNum(6)

print "The numbers:"

for num in numbers:
    print num

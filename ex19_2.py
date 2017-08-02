# -*- coding: utf-8 -*-
from sys import argv

script, t1, t2 = argv

def test(test1, test2):
    print "%s + %s = %s" % (test1, test2, test1 + test2)

a1 = 10
a2 = 50

# 1
test(20, 30)
# 2
test(a1, a2)
# 3
test(10 + 20, 5 + 6)
# 4
test(a1 + 100, a2 + 1000)
# 5
test(int(raw_input("test1: ")), int(raw_input("test2: ")))
# 6
test(int(raw_input("test1: ")) + 100, int(raw_input("test2: ")) + 1000)
# 7
test(int(raw_input("test1: ")) + a1, int(raw_input("test2: ")) + a2)
# 8
test(int(t1), int(t2))
# 9
test(int(t1) + 100, int(t2) + 1000)
# 10
test(int(t1) + a1, int(t2) + a2)

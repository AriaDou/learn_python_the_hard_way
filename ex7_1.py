# -*- coding: utf-8 -*-
# 输出字符串
print "Mary had a little lamb."
# 将'snow'以字符串的形式插入长字符串后，输出
print "Its fleece was white as %s" % 'snow'
# 输出字符串
print "And everywhere that Mary went."
# 连续输出10个"."
print "." * 10 # what'd that do?

#赋值end1-12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens:去掉逗号后会换行，不去掉会有空格
# 输出end1-6拼接而成的字符串,输出后带空格
print end1 + end2 + end3 + end4 + end5 + end6,
# 输出end7-12拼接而成的字符串，输出后换行
print end7 + end8 + end9 + end10 + end11 + end12

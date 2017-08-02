# -*- coding: utf-8 -*-
# 汽车总量:100
cars = 100
# 单车负载:4.0
space_in_a_car = 4.0 # 换成4，在当前使用情况下是没有问题的，只是计算出的数值都是整数，carpool_capacity会变成120
# 司机总量:30
drivers = 30
# 乘客总量:90
passengers = 90
# 未被驾驶的汽车 = 汽车总量 - 司机总量
cars_not_driven = cars - drivers
# 被驾驶的汽车 = 司机总量
cars_driven = drivers
# 总负载能力 = 被使用的汽车 * 单车负载
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车坐乘客数 = 乘客总量 / 被驾驶的汽车
average_passengers_per_car = passengers / cars_driven

# 有cars辆可用汽车
print "There are", cars, "cars available."
# 仅有drivers位司机
print "There are only", drivers, "drivers available."
# 今天将有cars_not_driven辆汽车空闲
print "There will be", cars_not_driven, "empty cars today."
# 今天我们可以运输carpool_capacity位乘客
print "We can transport", carpool_capacity, "people today."
# 我们有passengers位乘客要运送
print "We have", passengers, "to carpool today."
# 我们一辆车大约要运average_passengers_per_car位乘客
print "We need to put about", average_passengers_per_car, "in each car."

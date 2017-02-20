#没什么好注释的
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#1/2
y = "Those who know %s and those who %s." % (binary, do_not)

print x;
print y;

#3
print "I said: %r." % x
#4
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

#5
print w + e

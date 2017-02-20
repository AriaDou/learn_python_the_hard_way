name = "Zeds"
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
height_cm = height * 2.54
weight_kg = weight / 2.2046
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r cms tall." % height_cm
print "He's %d kgs heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d Iget %d." % (
 age, height, weight, age + height + weight
)

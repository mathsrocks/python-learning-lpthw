name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_2_cm = 2.54
pound_2_kg = 0.453592
inch = 50
pound = 200
no_2_round = 1.7333

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Acutally that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "%d inches = %d centimeters" % (inch, inch * inch_2_cm)
print "%d pounds = %d kilograms" % (pound, pound * pound_2_kg)
print "Representation of an integer: %r" % inch
print "After rounding, %f becomes %d." %(no_2_round, round(no_2_round))

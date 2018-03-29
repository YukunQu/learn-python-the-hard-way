my_name = 'Zed A.Shaw'
my_age_of_learning_code = 35
my_height = 74*2.54 #centimeters
my_weghit = 180*0.4536 #kg
my_eyes = 'Blue'
my_cloth = 'white'
my_hair = 'Brown'


print("let's talk about %s." % my_name)
print("he's %r centimeters tall."% my_height)
print("he's %r kilograms heavy."% my_weghit)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair."% (my_eyes,my_hair))
print("His cloth are usually %s depending on the coffee."%my_cloth)

#this line is tricky,try to get it exactly right
print("If I add %d,%d,and %d I get %r. "%(my_age_of_learning_code,my_height,my_weghit,my_age_of_learning_code+my_height+my_weghit))
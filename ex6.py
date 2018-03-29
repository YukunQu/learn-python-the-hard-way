x = "There are %d types of people."%10      # give variables x a string combining format string,string variables
binary = 'binary.'
do_not = "dont't"
y = "Those who know %s and those who %s."%(binary,do_not) # y alse to be a  string variables,can print a string combining two variables

print(x)
print(y)

print("I said: %r." %x)                     # the variable 'x' also can be used as part of a string.
print("I also said: '%s',"%y)               # different string word can be mixed like jigsaw.

hilarious = False
joke_evaluation = "Isn't that joke so funny?!%r"

print(joke_evaluation % hilarious)          # it seems like the upper one,but it print a boole value.

w = 'This is the left side of ...'
e = 'a string with a right side.'

print(w+e)                                  # it also is a string combining variables,but it connects two string into one string.
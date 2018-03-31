from sys import argv

script,filename =argv

#  get the name of file from user

txt = open(filename)

# using function--open() to extract a file object

print('Here is your file %r :'%filename)
print(txt.read())

#oh,another way to acquire the filename

print('Type the filename again:')
file_again = raw_input(">")

txt_again = open(file_again)

print(txt_again.read())


#from sys import argv

#script,filename =argv

#  print('Type the filename again:')
# file_again = raw_input(">")
from sys import argv

script,input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

    # seek function put pointer toward line you need it

def print_a_line(line_count,f):
    print(line_count,f.readline())

# define functions


#use those functions

current_file = open(input_file)

print('First let is print the whole file:\n')
print_all(current_file)

print('Now let is rewind,kind of like a tape')
rewind(current_file)

print("Let 's print three lines:")
i = 1
print_a_line(i,current_file)
i = i+1
print_a_line(i,current_file)
i = i+1
print_a_line(i,current_file)



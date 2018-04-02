from sys import argv
from os.path import  exists

script,from_file,to_file = argv
print('Copying from %s to %s'%(from_file,to_file))

input =  open(from_file)
indate = input.read()

print('The input file is %d bytes long'%len(indate))

print('Does the output file exist?%r'% exists(to_file))
print('Ready,hit return to continue,CTRL-C to abort.')
raw_input()

output = open(to_file,'w')
output.write(indate)

print('Alright,all done.')

output.close()
input.close()
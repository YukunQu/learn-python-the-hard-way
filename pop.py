
line_num=0
fp=open("test_orig.txt","r+")

while 1:
    buffer=fp.read(8*1024*1024)
    if not buffer:
        break
    line_num+=buffer.count('\n')
    print(line_num)

fp=open("test_orig.txt","r+")
i = 0
while i < line_num:
     x = fp.readline()
     list = x.split()
     print(list)
     i += 1
else:print ('over')
fp.close()
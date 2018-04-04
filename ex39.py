ten_things = 'Apples Oranges Crows Telephone Light Sugar'

#赋值ten things

print('Wait there is not 10 things in that list,let is fix that.')
#输出 ten things

stuff = ten_things.split()
#split函数将ten things 拆分为一块一块，并赋给stuff
print(stuff)
more_stuff = ["Day","Ngiht","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!= 10:
    next_one = more_stuff.pop()  #移除一个morestuff中最后一个元素
    print("Adding:",next_one)
    stuff.append(next_one)      #在stuff末尾添加nextone
    print("There is %d items now."%len(stuff)) # 输出目前stuff长度

print("There we go:",stuff)

print("Let is do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(''.join(stuff))
print('#'.join(stuff[3:5]))
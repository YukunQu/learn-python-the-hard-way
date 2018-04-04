def inumber(x,y):

    i = 0
    numbers = []

    while i < x:
        print("At the top i is %d" %i)
        numbers.append(i)
        i = i +y
        print("Numbers now:",numbers)
        print("At the bottom i is %d" %i)

        print("The numbers:")

    for num in numbers:
        print(num)

    print('fenjiexian')
    for c in  range(numbers[4]):
        print(c)

inumber(10,2)

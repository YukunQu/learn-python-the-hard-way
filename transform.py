
def tranform(x):
    F = int(x)
    C = C= 5/9 * (F - 32)
    return C

#print(tranform(input()))

for i in range(0,300,20):
    print(tranform(i))

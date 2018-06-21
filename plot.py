from math import sqrt


def isprime(x):
    if x == 1:
        return False
    elif x == 2 or x == 3:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
            else:
                return True


for i in range(1,100):
    if isprime(i):
        print(i)
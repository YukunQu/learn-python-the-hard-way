from math import sqrt

def isprime(n):  # 判断是否为素数
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def monisen(x):
    p = 2
    count = 0
    if x ==0:
        return
    else:
        while 1:
            if isprime(p):
                M = 2 ** p - 1
                if isprime(M):
                    count += 1
                    if count < x:
                        p += 1
                        continue
                    else:
                        break
                else:
                    p += 1
            else:
                p += 1
    return M

print(monisen(int(input())))


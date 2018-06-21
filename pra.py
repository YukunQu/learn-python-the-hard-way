'''def isPrime(n):
    i = 2
    while i < n // 2 + 1:
        if n % i == 0:
            return False
        i += 1
    return True
'''


from math import sqrt

def isprime(n):  # 判断是否为素数
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



'''m = 4
count = 0
while m < 2000:
    i = 2
    while i < m:
        if isPrime(i) and isPrime(m - i):
            count += 1
            if count % 6 != 0:
                print("{}={}+{}".format(m, i, m - i), end=" ")
            else:
                print("{}={}+{}".format(m, i, m - i))
            m += 2
            break
        else:
            i += 1
'''

print(isprime(2))
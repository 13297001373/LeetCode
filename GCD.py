#最大公约数
def gcd(a,b):
    while a%b!=0:
        tmp = b
        b = a%b
        a = tmp
    print(b)
    return b

if __name__ == '__main__':
    gcd(481,221)
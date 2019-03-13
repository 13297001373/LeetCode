def Fib(n):
    return n if n<=1 else Fib(n-1)+Fib(n-2)

if __name__ == '__main__':
    result = Fib(2)
    print(result)

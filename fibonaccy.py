

def fib(n):
    if (n == 0 or n == 1):
        return(n)
    return fib(n-2)+fib(n-1)

for i in (range (30)):
    print(fib(i))

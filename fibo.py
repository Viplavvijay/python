def fib(n):
    while (n > 0):
        if n == 1 or n == 2:
            return 1
        else:
            return fib(n-1)+fib(n-2)
b = int(input("enter the no."))
for i in range(1, b):
    print(fib(i), end=' ')
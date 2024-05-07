def fac(n):
    while(n>=0):
        if n== 1 or n==0:
            return 1
        else:
            return n*fac(n-1)
b=int(input("Enter the number "))
a=fac(b)
print(a)

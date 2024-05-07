def sum(n):
    while(n>=1):
        if n==1:
            return 1
        else:
            return n+sum(n-1)
b=int(input("Enter the number "))
a=sum(b)
print(a)
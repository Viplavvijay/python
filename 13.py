def primenumber():
    i=0
    a = int(input("Enter the lowest number to which you have to find prime numbers"))
    b = int(input("Enter the lowest number to which you have to find prime numbers"))

    print("The prime numbers between ",a," and ",b," are: ")
    for number in range(a,b+1):
        if number>1:
            for i in range(2,(number)):
                if number%i==0:
                    break
                else:
                    print(number," is a prime number")
print(primenumber())

sum=0

# for j in range(2,a+1):
#     sum = sum + primenumber()


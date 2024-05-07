arr = []
def pro(size):
    if size == -1:
        return 1
    else:
        return arr[size]*pro(size-1)

n = int(input("Enter the size of array: "))
for i in range(0, n):
    a = int(input("Enter a number: "))
    arr.append(a)
print("Product of the array is:",pro(n-1))
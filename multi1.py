def product(arr, n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return arr[0]*arr[1]
    else:
        return arr[n]*product(arr, n-1)
n = int(input("Enter the number of elements for list:")) 
a = []
for i in range(0, n):
    element = int(input("Enter element:"))
    a.append(element)
b = product(a, n-1)
print("The list is:", a) 
print("Product of items in list:", b)

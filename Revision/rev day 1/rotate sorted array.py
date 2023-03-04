def mini(arr, n):
    min=arr[0]
    for i in range(n):
        if arr[i]<min:
            min=arr[i]
    return min

l=[]
a=int(input("Enter the no of elements: "))
for i in range(0,a):
    ele=int(input("Enter the values: "))
    l.append(ele)
print(l)
n=len(l)
print(mini(l,n))

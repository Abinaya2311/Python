def repeat(arr, N):
    for i in range(N):
        for j in range(i + 1, N):
            if (arr[i] == arr[j]):
                return arr[i]
l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
N=len(l)
print(repeat(l,N))

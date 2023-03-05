def searchrange(num, target):
    start=-1
    end=-1
    for i in range(len(num)):
        if num[i]==target:
            if start==-1:
                start=i
            end=i
    return [start, end]
l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
l.sort()
print(l)
target=int(input("Target value: "))
print(searchrange(l, target))

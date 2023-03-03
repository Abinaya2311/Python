l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print('\n')
l.sort()
print(l)
l.sort()
if a%2==0:
    m1=l[a//2]
    m2=l[(a//2)-1]
    median=(m1+m2)/2
else:
    median=l[a//2]
print("Middle element: ",median)

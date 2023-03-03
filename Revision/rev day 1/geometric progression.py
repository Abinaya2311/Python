def geometric(li):
    if len(li) <= 1:
        return True
    ratio = li[1]/float(li[0])
    for i in range(1, len(li)):
        if li[i]/float(li[i-1]) != ratio: 
            return False
    return True
l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
print(geometric(l))

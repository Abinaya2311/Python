def sums(num, target):
    num.sort()
    result=[]
    for i in range(len(num)-3):
        if i and num[i] == num[i - 1]:
            continue
        for j in range(i+1, len(num)-2):
            if j!=i+1 and num[j]==num[j-1]:
                continue
            sum=target-num[i]-num[j]
            left, right=j+1, len(num)-1
            while left<right:
                if num[left]+num[right]==sum:
                    result.append([num[i], num[j], num[left], num[right]])
                    right-=1
                    left+=1
                    while left<right and num[left]==num[left-1]:
                        left+=1
                    while left<right and num[right]==num[right+1]:
                        right-=1
                elif num[left]+num[right]>sum:
                    right-=1
                else:
                    left+=1
    return result

l=[]
a=int(input("Enter number of elements: "))
for i in range(0,a):
    ele=int(input("Enter the value: "))
    l.append(ele)
print(l)
g=int(input("Enter the target value: "))
print(sums(l,g))

n=int(input("Enter number of rows: "))
k=10
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k, end=' ')
        if i==1 or j==1:
            k=5
        if i==3 or j==2:
            k=20
        if i==4 or j==3:
            k=10
    print()

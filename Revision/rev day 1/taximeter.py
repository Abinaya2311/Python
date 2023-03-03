def taximeter(km):
    if (km<=1):
        b=5
        print(b)
    elif km in range(1,6):
        b=10
        print(b)
    elif km in range(6,12):
        b=15
        print(b)
    elif km in range(12,18):
        b=20
        print(b)
    else:
        b=25
        print(b)
    return b
taxino=int(input("Enter the taxi number: "))
name=input("Enter passenger name: ")
km=int(input("Enter the distance travelled (in km): "))
print("Bill amount: "); taximeter(km)
    

from math import gcd
def lcm(x,y,z):
    a = gcd(x,y,z)
    num = x
    num2 = y * z // a
    LCM = num * num2 // a
    return LCM
x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))
print("LCM: ", lcm(x,y,z))
print("GCD: ",gcd(x,y,z))

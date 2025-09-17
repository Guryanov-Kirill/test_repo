def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
x = int(input())
y = int(input())
print(gcd(x, y))

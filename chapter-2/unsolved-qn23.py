def find_gcd(a,b):
    if a>b:a,b=b,a
    while b%a != 0:
        a,b = b%a, a
    return a

print(find_gcd(24, 30))
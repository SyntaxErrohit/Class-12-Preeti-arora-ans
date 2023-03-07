def find_gcd(a,b):
    if a>b:a,b=b,a
    if b%a==0: return a
    return find_gcd(b%a,a)

print(find_gcd(24,30))
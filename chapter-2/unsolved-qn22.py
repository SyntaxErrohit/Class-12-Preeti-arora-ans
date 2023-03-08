# Recursion
def add(n):
    if n==1:return 1
    if n%2 == 0:
        return add(n-1) + 1/n
    else:
        return add(n-1) - 1/n

print(add(5))

# Non-recursion
def add(n):
    s = 1
    for i in range(2, n+1):
        if i%2==0:
            s += 1/i
        else:
            s -= 1/i
    return s

print(add(5))
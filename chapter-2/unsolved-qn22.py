def add(n):
    if n==1:return 1
    if n%2 == 0:
        return 1/n + add(n-1)
    else:
        return -1/n + add(n-1)

print(add(5))
def multiply(l, t=0):
    if t < len(l):
        return l[t]*multiply(l, t+1)
    else:
        return 1
    
print(multiply((8, 2, 3, -1, 7)))
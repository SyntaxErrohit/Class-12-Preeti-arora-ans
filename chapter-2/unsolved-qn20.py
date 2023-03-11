def find_multiples(n, t=1):
    print(t*n)
    if t == 4:
        return 1
    else:
        return find_multiples(n, t+1)

find_multiples(6)
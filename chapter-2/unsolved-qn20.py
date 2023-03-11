def find_multiples(n, t=1):
    print(t*n, end=" ")
    if t == 4:
        print()
    else:
        find_multiples(n, t+1)

find_multiples(6)
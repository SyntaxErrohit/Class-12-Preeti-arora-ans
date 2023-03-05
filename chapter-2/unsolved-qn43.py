def displayPrime(N):
    for num in range(2, N):
        flag = True
        for i in range(2, num):
            if num%i == 0:
                flag = False
                break
        if flag:
            print(num)

N = int(input("Enter N: "))
displayPrime(N)
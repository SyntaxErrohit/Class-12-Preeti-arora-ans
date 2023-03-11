def check_prime(n):
    flag = True
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break

    if flag == True:
        return "{0} is a prime number".format(n)
    else:
        return "{0} is not a prime number".format(n)

print(check_prime(47))
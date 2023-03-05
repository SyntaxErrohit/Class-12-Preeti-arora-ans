def EvenSum(NUMBERS):
    summ = 0
    for i in NUMBERS:
        if i%2==0:
            summ += i
    return summ

n = int(input("Enter number of numbers: "))
t = ()
for i in range(n):
    t += (input(),)

s = EvenSum(t)
print("Sum of even numbers are:", s)
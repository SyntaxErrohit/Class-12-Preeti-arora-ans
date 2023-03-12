def avg(tup):
    s = sum(tup)
    l = len(tup)
    return s/l

n = int(input("Enter number of integers: "))
t = ()
for i in range(n):
    t += (int(input()),)
a = avg(t)
print(a)
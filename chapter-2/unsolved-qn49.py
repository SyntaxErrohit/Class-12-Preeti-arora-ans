def LeftShift(lst, x):
    return lst[x:] + lst[:x]

n = int(input("Enter number of elements in list: "))
l = []
for i in range(n):
    l.append(int(input()))

x = int(input("Enter x:"))
lnew = LeftShift(l, x)

print("Input list:")
for i in l:
    print(i, end=" ")
print()

print("Output list:")
for i in lnew:
    print(i, end=" ")
print()
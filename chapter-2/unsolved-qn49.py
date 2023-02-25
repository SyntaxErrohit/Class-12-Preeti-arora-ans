def LeftShift(lst, x):
    leftlst = lst[x:]
    rightlst = lst[:x]
    return leftlst + rightlst

print(LeftShift([20, 40, 60, 30, 10, 50, 90, 80, 45, 29], 3))
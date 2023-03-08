def sort_hyphen(string):
    l = string.split("-")
    l.sort()
    return "-".join(l)

inp = input("Enter sequence of words: ")
s = sort_hyphen(inp)
print("Output:", s)
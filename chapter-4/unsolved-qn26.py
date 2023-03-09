t = open("book.txt", "w")

while True:
    text = input("Enter line: ")
    if text == "END":
        break
    else:
        t.write(text)

t.close()

t = open("book.txt", "r")
data = t.readlines()
for i in data:
    if i[0].isupper():
        print(i)

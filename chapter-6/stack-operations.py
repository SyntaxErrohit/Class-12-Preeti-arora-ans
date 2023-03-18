stack = list()
size = 0

def push():
    item = input("Enter item: ")
    stack.append(item)
    size += 1
    return size

def peek():
    if size == 0:
        print("Underflow, Stack is empty")
    else:
        top = size - 1
        print(stack[top])

def isEmpty():
    if size == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")

def pop():
    if size == 0:
        print("Underflow, Stack is empty")
    else:
        item = stack.pop()
        size -= 1
        print("Item popped:", item)
        return size

def display():
    print("The stack is:")
    for i in range(size-1,-1,-1):
        print(stack[i])

ch = "y"
while ch == "y":
    print("Stack operation")
    print("1. Push")
    print("2. Peek")
    print("3. Is empty")
    print("4. Pop")
    print("5. Display")
    print("6. Exit")
    op = int(input("Enter option: "))
    if op == 1:
        size = push()
    elif op == 2:
        peek()
    elif op == 3:
        isEmpty()
    elif op == 4:
        size = pop()
    elif op == 5:
        display()
    elif op == 6:
        ch = "n"
    else:
        print("Wrong option. Try again.")

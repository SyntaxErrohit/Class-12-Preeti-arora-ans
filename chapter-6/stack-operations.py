stack = list()
size = 0

def push(item):
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
        print("tack is empty")
    else:
        print("Stack is not empty")





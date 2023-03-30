from lab3 import ArrayStack
def copyStack(stack1, stack2):
    chack = ArrayStack()
    while True:
        if stack1.is_empty():
            break
        else:
            data = stack1.pop()
            chack.push(data)
    while True:
        if stack2.is_empty():
            break
        else:
            stack2.pop()
    while True:
        if chack.is_empty():
            break
        else:
            data = chack.pop()
            stack1.push(data)
            stack2.push(data)

s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack(); s2.push(15)
s1.printStack()
s2.printStack()
copyStack(s1, s2)
s1.printStack()
s2.printStack()
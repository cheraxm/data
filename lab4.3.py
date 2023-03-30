from lab3 import ArrayStack
 
def infixToPostfix(expression):
    listt = ArrayStack()
    postfix = ""
    def compareOperator(operator):
        compare1 = compare2 = 0
        if operator in ["*", "/"]:
            compare1 = 2
        elif operator in ["+", "-"]:
            compare1 = 1
        if listt.stackTop() in ["*", "/"]:
            compare2 = 2
        elif listt.stackTop() in ["+", "-"]:
            compare2 = 1
        if compare1 > compare2:
            return True
        else:
            return False
    for i in expression:
        if i.isalpha():
            postfix += i
        elif i == "(":
            listt.push(i)
        elif i == ")":
            while listt.stackTop() != "(":
                postfix += listt.pop()
            listt.pop()
        else:
            if listt.is_empty():
                listt.push(i)
                continue
            while not listt.is_empty() and not compareOperator(i):
                postfix += listt.pop()
            listt.push(i)
    while not listt.is_empty():
        postfix += listt.pop()
    return postfix


exp = "A+B*C-D/E"
postfix = infixToPostfix(exp)
print("Postfix of "+exp+" is "+postfix)
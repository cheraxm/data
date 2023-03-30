"""DSA LAB 4.1"""

class ArrayStack : 
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True
    
    def push(self, data):
        return self.data.append(data)

    def pop(self):
        if len(self.data) != 0:
            self.data.pop()
        else:
            print( "Underflow: Cannot pop data from an empty list")

    def stackTop(self):
        if self.data != None:
            return self.data[-1]
        else:
            return None

    def printStack(self):
        print(self.data)



    def is_parentheses_matching(self, expression):
        stack = ArrayStack()
        for i in expression:
            if i == "(":
                stack.push(i)
            elif i == ")":
                if stack.is_empty():
                    print("Parentheses in " + expression + " are unmatched")
                    return False
                stack.pop()
        if stack.is_empty():
            return True
        else:
            return False


str = "(((A-B)*C)"
result = ArrayStack().is_parentheses_matching(str)
print(result)
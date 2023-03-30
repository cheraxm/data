"""DSA LAB 3"""

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
            return self.data.pop()
        else:
            print( "Underflow: Cannot pop data from an empty list")

    def stackTop(self):
        if self.data != None:
            return self.data[-1]
        else:
            return None

    def printStack(self):
        print(self.data)



# s = ArrayStack()
# s.push(10); s.push(20); s.push(30)
# s.printStack() #=> โปรแกรมแสดง [10, 20, 30]
# x = s.pop() #=> ถ้า print(x) จะแสดงค่าข้อมูล 30
# s.pop()
# s.printStack() #=> โปรแกรมแสดง [10]
# s.pop()
# print(s.is_empty()) #=> โปรแกรมแสดง True
# s.pop() #=> โปรแกรมแสดงข้อความ “Underflow: Cannot pop data from an empty list”

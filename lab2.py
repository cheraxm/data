"""  DSA LAB 2"""

class DataNode:
    def __init__(self,name=""):
        self.name = name
        self.next = None

class SinglyLinedlist: 
    def __init__(self):
        self.count = 0
        self.head = None
    
    def treverse(self):
        if self.head is None:
            print("This is an empty list.")
        else:
            namelist = []
            pos = self.head
            while pos != None:
                namelist.append(pos.name)
                pos = pos.next
            print('->'.join(namelist))
    
    def insertfront(self,data):
        pNew = DataNode(data)
        if self.head != None:
            pNew.next = self.head
        self.head = pNew
        self.count += 1
    
    def insertLast(self,data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
        pos.next = pNew
        self.count += 1

    def inserBefore(self,node,data):
        pNew = DataNode(data)
        pos = self.head
        while pos.name != node:
            prev = pos
            pos = pos.next
        if pos.next != None:
            pNew.next = prev.next
            prev.next = pNew
            self.count += 1
        else:
            print("Cannot insert, %s does not exist" %node)

    def delete(self,data):
        pos = self.head
        while pos.name != data:
            prev = pos
            pos = pos.next
        if pos != None:
            prev.next = pos.next
            self.count -= 1
        else:
            print("Cannot delete, %s does not exise" %data)

        
    


        
mylist = SinglyLinedlist()
pNew = DataNode("Tony")
mylist.head = pNew
mylist.treverse()
pNew = DataNode("Kim")
mylist.head.next = pNew
mylist.treverse()
mylist.insertfront("bibi")
mylist.treverse()
mylist.insertLast("Chaaim")
mylist.treverse()
mylist.inserBefore("Tony","Youngyeans")
mylist.treverse()
mylist.delete("Kim")
mylist.treverse()
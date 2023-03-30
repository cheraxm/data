"""Binary Search Tree LAB 5-6"""

class BSTNode:
    def __init__(self, input_data):
        self.input_data = input_data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False

    def insert(self, data):
        pNew = BSTNode(data)
        prev = None
        start = self.root
        if self.is_empty():
            self.root = pNew
        else:
            while start != None:
                if data < start.data:
                    start = start.left
                    print("วิ่งซ้าย")

                else:
                    prev = start
                    start = start.right
                    #เชื่อมโหนด -> เช็คเงื่อนไข
            prev.right = pNew
        return

        #// insert input_data into BST

    def delete(self, data):
        del self.data
        #// delete input_data from BST
        return

    def preorder(self, root):
        if (root != None):
            print("->", root.input_data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            return

    def inorder(self, root):
        if (root != None):
            self.inorder(root.left)
            print("->", root.input_data, end=" ")
            self.inorder(root.right)
            print()

    def postorder(self, root):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.input_data, end=" ")
        #// postorder traversal

    def traverse(self) :
        if self.root == None:
            print("Empty Tree")
        else:
            print("Preorder:")
            self.preorder()
            print("Inorder:")
            self.Inorder()
            print("Postorder:")
            self.postorder()
        #// call preorder(), inorder(), postorder()

    def findMin(self) :
        #// return minimum value
        return

    def findMax(self) :
        #// return maximum value
        return


myBST = BST()
myBST.insert(16)
myBST.insert(30)
myBST.insert(10)
myBST.delete(30)
myBST.traverse()
print(myBST.is_empty())
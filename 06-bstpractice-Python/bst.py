# import sys
# sys.setrecursionlimit(10**6) 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, d):
        if self.root.value == d:
            return False
        elif d < self.root.value:
            if self.root.left:
                self.root = self.root.left
                return self.insert(d)
            else:
                self.root.left = Node(d)
                return True
        else:
            if self.root.right:
                self.root = self.root.right
                return self.insert(d)
            else:
                self.root.right = Node(d)
                return True

    def printSelf(self):
        # Your code goes here
        # pass
        if self.root is None:
            print("None")
        else:
            print(self.root.left)
            print(self.root.right)
        
    def search(self, find_val):
        # Your code goes here
        pass
        # if self.root is None or self.root.val == find_val: 
        #     return self.root 
        # if self.root.val < find_val: 
        #     return search(self.root.right,find_val) 
        
        # return search(root.left,find_val)

tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.printSelf()
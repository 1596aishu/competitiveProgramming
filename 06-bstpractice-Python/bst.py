class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert_bst(self, root, val):
        if root is None: 
                root.value = val 
        else: 
            if self.root.value < val: 
                if self.root.right is None: 
                    self.root.right = val 
                else: 
                    self.insert_bst(self.root.right, val) 
            else: 
                if self.root.left is None: 
                    self.root.left = val 
                else: 
                    self.insert_bst(self.root.left, val)

    def insert(self, new_val):
        self.insert_bst(self.root,new_val)

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


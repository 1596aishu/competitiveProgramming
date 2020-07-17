class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        # pass
        if self.root.value == None:
            self.root.value = new_val
        else:
            if new_val < self.root.value:
                self.root.left = insert(self.root.left, new_val)
            else:
                self.root = self.root.right
                

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass


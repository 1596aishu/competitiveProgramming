class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert_bst(self, root, node):
        if root is None: 
                root = node 
        else: 
            if root.value < node: 
                if root.right is None: 
                    root.right = node 
                else: 
                    self.insert_bst(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    self.insert_bst(root.left, node)

    def insert(self, new_val):
        self.insert_bst(self.root,new_val)
        # Your code goes here
        # pass
        # if self.root.value == None:
        #     self.root.value = new_val
        # else:
        #     if new_val < self.root.value:
        #         insert(root.left, new_val)
        #     else:
        #         insert(root.right, new_val)

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        # pass
        if (self.root.value == None):  
            return False
        if self.root.value == find_val:
            return True
        else:
            lef= self.search(self.root.left)
            if lef:
                return True
            rgt= self.search(self.root.right)
            return rgt

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        # pass
        self.preorder_print()



    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        # pass



    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        # pass
        if self.root:
            print(self.root.value)
            self.print_tree(root.left)
            self.print_tree(root.right)

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
        # self.insert_bst(self.root,new_val)
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
        pass
        # if self.root is None:
        #     print("None")
        # else:
        #     while self.root!=None:
        #         print(self.root.value)
        #         while self.root.left:
        #             self.root = self.root.left
        #             return self.printSelf()
        #         while self.root.right:
        #             self.root = self.root.right
        #             return self.printSelf()
        
    # def search(self, d):
        # Your code goes here
        pass
        if self.root is not  None and self.root.value:            
            if self.root.value == d:
                return True
            elif d < self.root.value and self.root.left is not None: 
                self.root = self.root.left
                return self.search(d)
            elif d > self.root.value and self.root.right is not None:
                self.root = self.root.right
                return self.search(d)
            return False
        return False 
        # if self.root is None or self.root.val == find_val: 
        #     return self.root 
        # if self.root.val < find_val: 
        #     return search(self.root.right,find_val) 
        
        # return search(root.left,find_val)

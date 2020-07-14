"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append = new_element


    def peek(self):
        # pass
        return self.storage[0]
         

    def dequeue(self):
        a = self.storage[0]
        for i in range(len(self.storage)-2):
            self.storage[i] = self.storage[i+1]
        self.storage[len(self.storage)-1] = None
        return a



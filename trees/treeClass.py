class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
    
    def insertLeftVal(self, val):
        self.left = Node(val)
    
    def insertRightVal(self, val):
        self.right = Node(val)
    
    def insertLeftNode(self, node):
        self.left = node
    
    def insertRightNode(self, node):
        self.right = node

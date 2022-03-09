'''
problem:
implement a stack with a max feature

solution:
maintain two stacks, one that tracks the stack 
and one that tracks the max.

key is that the max-stack does not need to store
all the values
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_track = []
    
    def push(self, x):
        if (len(self.max_track)== 0) or (x >= self.max_track[-1]):
            self.max_track.append(x)

        self.stack.append(x)
    
    def getMax(self):
        return self.max_track[-1]

    def pop(self):
        x = self.stack.pop()
        if x == self.max_track[-1]:
            self.max_track.pop()
    
    def printStacks(self):
        print("internal stack = " + str(self.stack))
        print("internal max = " + str(self.max_track))
    

if __name__ == "__main__":
    calls = [("push", 1),
        ("push", 3),
        ("pop"),
        ("push", 2),
        ("push", 0),
        ("push", 5),
        ("pop"),
        ("pop")
    ]

    newStack = MaxStack()
    for x in calls:
        if x[0] == "push":
            print("   push")
            newStack.push(x[1])
        
        else:
            print("   pop")
            newStack.pop()
        
        print("current max = " + str(newStack.getMax()))
        newStack.printStacks()

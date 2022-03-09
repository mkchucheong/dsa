class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def traverse_print(self):
        tail = ListNode(data = self.data, next = self.next)
        while tail:
            print(tail.data, end=', ')
            tail = tail.next
        
        print()
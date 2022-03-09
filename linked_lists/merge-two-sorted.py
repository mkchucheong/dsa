from ll_class import ListNode

'''
framework:
program that takes two [sorted] linked lists, returns their merge

approach:
traverse both lists, and choose the node containing the smaller key to continue traversing

notes:
when we set output_head = tail = ListNode(data=0), what's happening here 
is that they are both pointing to the same object.
Later on, when tail gets updated, note that we first change what tail.next
is pointing to.
This changes the structure of the output_head linked list.
Then when we update tail, we just move along the chain.
'''

def merge_sorted_ll(listA, listB):
    output_head = tail = ListNode(data=0)

    # iterating through both LLs until we reach the end of one
    while listA and listB:
        if listA.data <= listB.data:
            tail.next = listA
            listA = listA.next
        else:
            tail.next = listB
            listB = listB.next
        
        tail = tail.next
        print("currently the tail = ")
        tail.traverse_print()
        print("currently the head = ")
        output_head.traverse_print()
    
    if listA:
        tail.next = listA
    elif listB:
        tail.next = listB
    
    return output_head.next

if __name__ == "__main__":
    l1 = ListNode(5)
    l1 = ListNode(2, next=l1)
    l1 = ListNode(1, next=l1)

    l2 = ListNode(6)
    l2 = ListNode(4, next=l2)
    l2 = ListNode(3, next=l2)

    l1.traverse_print()
    l2.traverse_print()

    out_ll = merge_sorted_ll(l1, l2)
    out_ll.traverse_print()
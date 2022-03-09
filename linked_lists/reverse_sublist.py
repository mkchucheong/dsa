from ll_class import ListNode

'''
framework:
program that takes two [sorted] linked lists, returns their merge

approach:
traverse both lists, and choose the node containing the smaller key to continue traversing

notes:
'''

def merge_sorted_ll(listA, listB):
    output_head = tail = ListNode(data=0)
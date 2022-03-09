'''
write a program  that takes an array A, and an index i into A,
and rearranges the elements such that all elements less than A[i]
appear first, followed by elements equal to the pivot, and
followed by elements greater than the pivot
'''

# solving in O(n) time, with O(1) space
# approach: swap elements, putting elements less than pivot at start
# and elements greater than pivot at the end
def partition_flag(arr, idx):
    pivot = arr[idx]
    
    lower = 0
    greater = len(arr)
    i = 0

    while i < greater:
        if arr[i] < pivot:
            arr[lower], arr[i] = arr[i], arr[lower]
            lower += 1
            i += 1
        elif arr[i] == pivot:
            i += 1
        else:
            greater -= 1
            arr[greater], arr[i] = arr[i], arr[greater]
    
    return arr

if __name__ == "__main__":
    a = [1, 3, 4, 2, 1, 5, 3, 2, 1]
    idx = 2
    print(partition_flag(a, idx))
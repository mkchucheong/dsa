'''
public class Deque<Item> implements Iterable<Item> {

    // construct an empty deque
    public Deque()

    // is the deque empty?
    public boolean isEmpty()

    // return the number of items on the deque
    public int size()

    // add the item to the front
    public void addFirst(Item item)

    // add the item to the back
    public void addLast(Item item)

    // remove and return the item from the front
    public Item removeFirst()

    // remove and return the item from the back
    public Item removeLast()

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator()

    // unit testing (required)
    public static void main(String[] args)

}
'''

# with stacks
class Deque:
    def __init__(self):
        pass

# with array
class Deque:
    def __init__(self):
        self._scale = 2
        self._capacity = 4 # initially
        self._arr = [0]*self._capacity
        self._head = 0
        self._tail = 0
        self._num = 0
    
    def isEmpty(self):
        return self._num == 0
    
    def size(self):
        return self._num
    
    # add to head
    # [1, 2, 3] : 4 -> [1, 2, 3, 4]
    def addFirst(self, x):

        # if we have enough elements, then we need to resize the array
        if self._num == self._capacity:
            pass

    # add to tail
    # [1, 2, 3] : 4 -> [4, 1, 2, 3]
    def addLast(self, x):
        pass

    # remove from head
    # [1, 2, 3, 4] -> [1, 2, 3]
    def removeFirst(self):
        result = self._head
        self._num -=1 

        # account for wraparound
        if self._head < 0:
            self._head = len(self._arr) - 1
        
        return result

    # remove from tail
    # [1, 2, 3, 4] -> [2, 3, 4]
    def removeLast(self):
        result = self._arr[self._tail]
        self._num -= 1

        # account for wraparound
        self._tail = (self._tail + 1) % (len(self._arr))

        return result





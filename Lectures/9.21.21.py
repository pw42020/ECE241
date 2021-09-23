'''
Lecture 8: Lists
    Lists
        used Python lists to implement abstract data types
        Not included by all programming languages
        List is collection of items where each holds relative position (first item, second item, third item, etc.)
        Simple unsorted lists for scores: 54, 26, 93, 17, 77, 31
    Linked List
        LOOK UP LATER LMFAO
    Unordered List
        Build from collection of nodes
            Each linked to the next by reference
        Must contain reference to first node
        mylist points to none which points to ground
            Then you fill it up using .add for each number

'''
def add(self,item): #in class Node
    temp = Node(item)
    temp.setNext(self,head) #setting new head pointer as new appended number
    self.head = temp
def size(self):
    current = self.head
    count = 0
    while current != None:
        count += 1
        current = current.getNext()
    return count
def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
        if current.getData == item:
            found = True
        else:
            current = current.getNext()
    return found
def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            previous = current.getNext()
    if previous == None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext())
'''
    Unsorted List: Remove
        Two step approach
            Find
            Remove
        How to remove node:
            Remove node
            Use previous and current
'''
class OrderedList:
    def __init__(self):
        self.head = None
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
'''
    Lecture 6: Hashing
        Hashing
            Data structure that can be searched in O(1) time
            Need to know more about where items are when searched for in collection
            Single comparison if item is where it should be
        Hash Table
            Collection of items stored in a way which makes them easy to find later
            Position in hash table often called slot
                Holds an item
            Implement hash table using list
            Named using integer values
            Each element initialized to special Python value None
            Hash table of size m = 11
                m slots
                Named 0 through 10
        Hash function
            Mapping between item and slot where it belongs in is called hash function
        Example
            Set of integer items 54, 26, 93, 17, 77, and 31
            "remainder method" takes item and divides it by table size => h(item) = item%11
            Ex. 54mod11 is 10 so it goes in 10
            26%11 is 4 so it goes in 4
            lambda is the load factor (numberofitems/tablesize)
            Use has function to compute slot name and check if item is present
            Collision is if x1,x2%11 = y1
            
'''
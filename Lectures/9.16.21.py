'''
Lecture 5: Data Structures in Python
    Data Structures
        Stack, Queue, List, Dictionary, Matrix
    Objective
        Learn about different type of data structures and how they can be implemented in Python
        Learn about the interplay between data structure and algorithms
        Be able to implement data structures to enable the efficient performing of algorithms
    Linear Data Structures
        Examples: stacks, queues, dequeues, and lists
        Data collections of ordered items
        Order depends on how items are added and removed
        Once added item stays in position
        Characteristics
            Two ends (left-right,front-rear)
            Linear structures distinguished by how items are added and removed
            E.g. additions of new items only allowed at the end (queue)
            Appear in many algorithms
    Stack
        ordered collection of items
        Addition/removal of items always takes place at the same end (top)
        Base represents bottom and contains item has been in stack the longest
        Most recently added to be removed first (LIFO)
        Top: newer items; bottom: older items
    Applications using Stacks
        Check if delimiters are matched
            Match of opening and closing symbols: {},[],()
    Stack - Abstract Data Type
        Stack() creates a new, empty stack; no parameters and returns and emtpy stack
        push(item) adds a new item at the top of the stack; needs the item and returns nothing
        pop()
    Stack Analysis
        Abstract data type
            Change physical implementation while maintaining logical characteristics
        append() and pop() operations are both O(1)
        insert(0) and pop(0) operations both require O(n) for a stack of size n
        Very different timings
    Queue
        Ordered collection of items
        Add items on one end
        Remove items on the other end
        Item starts at the rear and makes its way to the front => FIFO
    Queue - Abstract Data Type
        Queue() creates a new, empty queue; no parameters and returns an empty queue
        enqueue(item) adds a new item to rear of queue; needs the item and returns nothing
        dequeue() removes front item; needs no parameters, returns item, queue is modified
        isEmpty() test if queue is empty; needs no parameters, returns a boolean
        size() returns number of items in the queue; needs no parameters; returns an integer
    Dequeue
        Very similar to queue
        But items can be added at front and rear
        Same for removing items
        Does not require FIFO and LIFO
    Lists
        Used Python lists to implement abstract data types
        Not included by all programming languages
        List is a collection of items where each holds relative position (first ite, second item, third item, etc.)




'''
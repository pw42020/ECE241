'''
Lecture 3: Heap Sort and Quick Sort
    Objective
        Learn how performance of merge sort can be further improved by using Heap sort
        and Quick Sort
    Heap Sort
        Use "heap" data structure to manage information
        Also makes an efficient priority queue (more later in the semester)
    Binary Heap
        Represent tree as single list:
            Root of tree is A[1] with index i of node
            PARENT(i)
                return [i/2]
            LEFT(i)
                return 2i
            RIGHT(i)
                return 2i+1
    Max-heap
        A[PARENT(i)]>A[i]
        Smallest value stored at root
        Subtree rooted at node contains no values smaller than value of node itself
    Heapsort - Analysis
        Heapsort takes time O(n |g n)
        BUILD-MAX-HEAP takes time O(n)
        MAX-HEAPIFY takes time O(|g n)
    Quick Sort
        Divide and conquer as in Merge Sort
        No additional storage use => overcomes Merge Sort weakness
        Trade-off: Performance diminished if list can be divided in half
        Pivot Value
            Simply first item in list
            Assist with splitting list
            Split point used to divide list for subsequent calls
    A[i],A[j]=A[j],A[i] -- Unpacking Syntax


'''
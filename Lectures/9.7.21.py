'''
Lecture 2: Asymptotic Notation, Insertion sort, and merge sort

Performance is Important
    Algorithm might run on very large data set
    Be efficient in terms of CPU and memory usage
        1. Look at sorting algorithms of different efficiency
        2. Learn how efficiency of algorithm can be determined
Asymptotic Analysis of Algorithms
    Algorithm complexity
    Asymptotic analysis
    Practical use
    Code examples
    "Big O" notation extracts essence of algorithm performance
        Defines an upper boundary on complexity growth
    ***Definition: f(x) = O(g(x)) for x-->inf.
        if and only if there is a positive real number m and a real number x0 such that
        f(x) <= m*g(x) for all x>x0
            for all x beyond x0, f(x) is bounded by m*g(x)
Practical use of asymptotic analysis
    Constants and lower degrees are ignored
        e.g. n/2 is O(n); 3n^2 + 15n is O(n^2)
Insertion sort
    Sorting is required in many applications
    Idea of insertion sort:
        Insert next element into partially sorted array
        Iterate
    Insertion requires shifting of elements
Merge sort
    Divide and conquer to improve performance
    Recursive algorithm
        Continually splits in half
            List is empty or has one item --> sorted by definition
            List has more than one item --> split and recursively involve merge sort
        Merge: taking two smaller lists and combining them together


'''
def insertionSort(alist): #insertion sort list
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1] #drops next position down to remove blank space in list
            position = position -1
        alist[position] = currentvalue #changes value

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
insertionSort(alist)
print(alist)
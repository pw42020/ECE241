'''
Lecture 8: Binary Serach Tree
    Objective
        Understand the structure of trees
        Understand the principles and be able to implement binary search trees
    Searching
        Algorithmic process of finding a particular item in a collection of items
        Returns True or False, and (sometimes) location of item
    Linear (Sequential) Search
        When data stored in collection such as list => linear or sequential relationship
        Each data item stored in position relative to others
        In Python: Relative positions are index values of individual items
        Start at first item, move from item to item until
            Item is found *OR*
            run out of items => item not in list
    Linear Search Analysis
        If item is not in list => n comparisons
        If item is in list:
            Best case: find item in first place
            Worst case: n comparisons
            So O(n)
    Linear Search Analysis: Ordered
        So far items were randomly placed in list
        What happens if list is ordered?
            No advantage if element is in list
            If element is NOT in list search can abort after item is larger than the one serached for
    Binary Search
        Take greater advantage of ordered list with clever comparisons
        Start examining the middle item
            The one searching for -> done
            Change to upper half if mid < number, lower half if otherwise
    Binary Search: Analysis
        Each comparison eliminates about one half of remaining items from consideration
        Start with n items, n/2 items left after 1st comparison
        Ith item => n/2^i
        O(logn)
    Tree Data Structures
        New Data Structure
            "2 dimensional"
            Easy access (similar to binary search in array)
            Easy insert and removal (similar to linked list)
        Trees
            Consist of nodes and linked
            Are graphs without loops
            Typically have a root node
    Structure of Trees
        Nodes
            Special node at top: root
        Links
            Connect nodes
            Zero or more nodes connected to a node
        Nodes can store information
    Tree Terminology
        Root: top node
        Parent: node above
            Every node (except root) has exactly one parent
        Child: node below
            Nodes may have zero or more children
            Binary trees have at most two children
        Leaf: node without children
        Subtree: tree below a given node
            That node becomes root of the subtree
        Level: distance from root
    Binary Trees
        Every node has at most two children
            Left and right child
        Binary search tree
            Nodes are arranged in a particular fashion
                Left subtree has values smaller than node
                Right subtree has values larger than node
    Binary Search Tree
        Mapping from key to value
            Binary search on list
            Search on hash tables
        Binary search tree
            Yet another way to map from key to value
            Not interested in exact placement of item
            Using binary tree structure for efficient searching
    Map: Abstract Data Type
        Map() creates a new, empty map; returns an empty map collection
        put(key, val) adds a new key-value pair; if key already in map, replace old with new value
        get(key) returns value stored in map or none otherwise
        del delete key-value pair
        Benefit: given key lok up associated data quickly
        Implementation that supports efficient search
        Hash table potentially O(1) performance
    Search Tree Implementation
        BST property:
            Key smaller than parent => left
            Key larger than parent => right
        BST property will guide implementation based on Map ADT




'''
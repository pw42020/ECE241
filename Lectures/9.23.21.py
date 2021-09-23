'''
Lecture 7:
    Overview
        Hash table, hash functions, collision resolution, Map data type, Analysis of hashing
    Objective
        Understand the principles of hash tables and hash functions
        Learn how to resolve collisions in hash functions
        Be able to implement hash tables and hash functions
    Hash table
        Implement hash table using list
        Each element initialized to special Python value None
        Hash table of size m = 11
            m slots
            Named 0 through 10
    Hash function
        Mapping between item and slot where it belongs in is called hash function
        Function take any item in collection and return integer in range of slot names (0,1,...m-1)
    Perfect Hash Function
        Function that maps each item into a unique slot
        Perfect hash function can be constructed if items never change
        No systematic way to construct perfect hash function given arbitrary collection
    Collision Resolution
        How to place two items in hash table if they hash to same slot?
        Since avoiding collisions is impossible, collision resolution is essential
    Open Addressing
        Try to find another open slot to hold item causing collision
        Start at original hash position and sequentially move through slots (loop around to start to cover entire table)
        Systematically probing each slot  one at a time => LINEAR PROBING
        Add one until you find an open slot
    Collision Resolution: Search
        Look up 93
        Hash value => 5
        Slot value => 93
    Look up 23
        Hash value => 9
        Slot value => 31
        Sequential search starting at index 10
        Find 20 or empty slot
    Collision Resolution: Slot Skipping
        Skip slots
            More evenly distribute items that have caused collision
            Reduce clustering
    Collision Resolution: Quadratic Probing
        Rehash function that increments have value by 1,3,5,7,9
        H, h+1, h+4, h+9, h+16
        Quadratic probing uses skip of successive squares
    Chaining
        Many items at same location
        Search" use hash function then search to decided whether item is present
    Implementing Hash Table
        Dictionary => data type to store key: value pairs
        Key is used to look up associated data value
        Often referred to as map
    (CHECK OUT MD5)
    (COMMON GOOGLE CODING INTERVIEW QUESTIONS)

'''
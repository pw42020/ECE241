"""
Lecture 9: Balanced Search Tree
    Objective
        Understand the principles of binary search trees that assure that tree remains balanced at all times
    Binary Search Tree Problem
        Unfortunately, search tree of height n can be constructed by inserting keys in sorted order
        In this case, performance of put() method is O(n)
    Balanced Binary Search Tree
        Special kind of binary serach tree
        Automatically assures that tree remains balanced at all times
        Tree is called AVL tree
        AVL tree implements Map ADT just like regular binary search tree
        Difference lies in its performance
        Need to keep track of balance
            Height of left and right subtree of each node
            balanceFactor = height(leftSubTree) - height(rightSubTree)
    


"""
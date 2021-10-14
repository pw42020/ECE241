"""
Lecture 11: Dynamic Programming
    Dynamic Programming
        Strategy to solve optimization problems
        Example: 63 cents need to be dispensed, what do you dispense to lose the least amount of coins?
    Greedy Method
        Start with largest coin and use as many of those
        Then next smaller one, and so on
        Will always work but is not always the most efficient solution
    Recursive Approach
        Minimum of a penny/nickel/quarter plus
        numCoins = min{1+numCoins(originalamount-1),....}
        Algorithm is extremely inefficient
        Takes 67,716,925 recursive calls to find solution
        Each node in the following graph corresponds to recMC()
        Label in node indicates amount of change for calculation
        Allows indicate coin just used
        Lot of redundancy
            e.g. make change for 15 cents done 3 times
        Key component to cutting down computation overhead: Remembering past results
            Avoid re-computing already known results
        Store results for minimum number of coins in table that solves problem
        Still holes in the table but recursive calls brought down to 221
        Called memorization or caching
    True Dynamic Programming Algorithm
        Start with making change for 1 cent
        Work our way up to amount of change we require
        Guarantees
            At each step of algorithm minimum number of coins to need to make
            change for any smaller amount already known
        Not a recursive function
Intro to Graphs
    Graphs
        More general structure than trees
            Tree is a special type of graph
        Computer can understand roadmap as a graph
        Computer can use graph representation to determine
            Shortest/Easiest/Quickest Path
    Formally define graph
        Graph can be represented by G, where G = V,E
        V is a set of vertices, and E is a set of edges
        Each edge is a set of tuples where w,v are in V
        Weight can be added as third component of a tuple
        A subgraph is a set of edges e and vertices v such that e is a subset of E and v is a subset of V


"""
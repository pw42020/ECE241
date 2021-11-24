'''
Lecture 15 (ish)?: Routing
    Routing - Intro
        Distributed Approach
            Each node computes best path without full view
            Shortest path computed as link information is exchanged
            "Distance vector algorithm"
    Distance Vector Algorithm
        Features
            Distributed, Iterative, Asynchronous
        Each node reports local view
            Cost to neighbors
            Routes to others via neighbors
        Each node picks the best option
            Bellman-Ford Equation
        Information is exchanged as distance vector
            Shortest distance to all nodes as seen locally
        With enough exchanges, routing converges
        Bellman-Ford Equation (Dyanmic Programming)
            dx(y) = cost of least cost path from x to y
            Then dx(y) = min{c(x,v) + dv(y)}
                min = min taken over all neighbors of v of x
                c(x,v) cost to neighbor v
        Node x:
            Knows cost to each neighbor v
            Maintains its neighbor's distance vector. For each neighbor it maintains
                Dv = [Dv(y): y in N]
        Iterative, asynchronous:
            Each local iteration caused by local link cost change or DV update message from neighbor
        Distributed
            Each node notifies neighbor only when DV changes
                Neighbors then notify their neighbors if necessary
    Prim's Spanning Tree Algorithm
        Consider problem that games designers and Internet radio providers face
        Efficiently transfer information to anyone who may be listening
            Gaming: Game state ( e.g. player positions) known at each player
            Radio: client receive data to play content
    In-network Duplication
        flooding: when node receives proadcast packet, sends copy to all neighbors
            problems: cycles and broadcast storm
        controlled flooding: node only broadcasts pkt if it hasn't broadcast same packet before
            node keeps track of packet ids already broadcasted
            or reverse path forwarding (RPF): only forward packet if it arrived on shortest path between node and source
    Spanning Tree
        First, construct spanning tree
        Nodes then forward/ make copies only along spanning tree
    Spanning Tree Creation
        Center node
        Each node sends unicast join message
Depth First Search (DFS)
    Knight's Tour Problem
        Puzzle played on chess board with single figure, the knight
        Objective: find sequence of moves that allow knight to visit every square on board "exactly" one
        Such sequence is called "tour"
        Upper bound on possible tours is 1.35*10^35
        Use graph search to solve problem
    Solve problem by using two mains steps:
        Represent legal moves of knight on chessboard as graph
        Use a graph algorithm to find path of length rows*(columns-1) where every vertex
            on graph is visited exactly once
    Complete Graph
        336 edges
        Less connections for vertices on edges of board
        Sparsity:
            Fully connected graph: 4096 edges
            Matrix only 8.2% filled
    DFS - Coloring
        DFS uses colors to keep track of which vertices have been visited
            White: unvisited
            Gray: visited
        Since DFS is recursive, use stack to help with backtracking
        After return from knightTour with status False:
            Remain inside while loop
            Look at nextvertex in nbrlist
    Knight's Tour - Analysis
        Number of nodes in binary tree is S^(N+1) - 1
        Number much larger for tree with up to 8 nodes
        Use average branch factor to estimate number of child nodes: k^(N+1) - 1, k is averge branching factor
        Example
            5x5 board, tree is 25 levels deep, N = 24
            = 3.12*10^14
        Way to speed up 8x8 case => runs in less than 1 seconds
        orderbyAvail will be called used instead of u.getConnections
        Line 10 is critical one, it ensures to select vertex that has fewest available moves
        But why not select node that has most available moves?
    General Depth First Search
        Implementation extends graph class by adding:
            Time instance variable and methods dfs and dfsvisit
            dfs method iterates over all vertices in graph calling dfsvisit on white nodes
            This ensures all nodes in graph are considered and no vertices are left out of depth first forest
        DFS method starts with single vertex startVertex and explores all neighboring white vertices as deeply as possible
        dfsvisit is almost identical to bfsexcept
        dfsvisit uses a stack where bfsexcept uses queue
            Not visible in code but implicit of dfsvisit
        Start and finishing times are called parentheses property
        All children of particular node in DFS
            Have later discovery time than parent
            Have earlier finish time than parent
        Figure shows final tree constructed by DFS algorithm





'''
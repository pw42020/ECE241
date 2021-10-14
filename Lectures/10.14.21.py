'''
Lecture 11: Vertex Classes and Graph Traversal
    Graphs Class
        Contains dictionary that maps vertex names to vertex objects
        Class also provides methods for adding and connecting vertices
        getVertices() returns names of all vertices in graph
        __iter__ allows iteration over particular graph
    Sparcity of Matrix
        Analysis:
            5,110 four-letter words
            Adjaceny matrix would have 5,110^2 cells
            Graph created by buildGraph()
    Implementing Breadth First Search
        BFS is one of the easiest algorithms to search a graph
        Given a graph G and starting vertex s BFS explores edges in the graph to find all
            vertices for which there is a path from s
        NoteL BFS finds all vertices at distance k from s before any vertices at distance k+1
        To visualize BFS, imagine that it is building one level at a time
        BFS adds all children of the starting vertex
        Then it begins to discover any of the grandchildren
        To keep track of progress edges are colored white gray or black
            White: undiscovered vertex
            Gray: initially discovered
            Black: vertex is colored black when completely explored


'''
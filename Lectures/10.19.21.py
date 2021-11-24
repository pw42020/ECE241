'''
Lecture 13:
    Shortest Path Problems
        When you surf the web, send email, or chat, lots of work is going on behind the scenes
        When web page is requested from server, request travels over local network on to the
            internet via a router
        Request travels over internet and eventually arrives at router that connect local
            are network where web server is located
        Web page travels same route back to client
        Many additional routers are inside internet "cloud"
        Routers work together to get information (data packets) from place to place
        Represent network of routers as graph with weighted edges
        Problem to solve
            Find path with smallest total weight
        Similar to BFS but here we are concerned with the total weight of the path rather than the number of nodes in path
        If all weight are equal, problem is the same
    Link State Algorithm
        Just use Dijkstra's Algorithm (find shortest path with weights)


'''
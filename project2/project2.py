from Graph import *
import random
from PriorityQueue import *
import sys
import copy


class ISPNetwork:

    def __init__(self):
        self.network = Graph()
        self.MST = Graph()

    def buildGraph(self, filename):
        f = open(filename, "r")
        data = f.readlines()

        for i in range(len(data)):  # getting all Vertexes set in network
            data[i] = data[i].split(",")
            data[i][2] = float(data[i][2])  # changing weight into float to make easier to use later

            if data[i][0] not in self.network:  # if vertex isn't already in network, adding it
                self.network.addVertex(data[i][0])

        for j in range(len(data)):
            self.network.addEdge(data[j][0], data[j][1], data[j][2])  # adding edge for each graph vertex

    def pathExist(self, router1, router2):

        routers = [self.network.getVertex(router1)]  # initializing routers for while loop
        router2 = self.network.getVertex(router2)  # changing router2 into a router for convenience sake
        lis = []
        usedlist = []

        if router1 is None or router2 is None:  # in case either router given is just NoneType

            return False

        while True:

            for i in range(len(routers)):

                for connection in routers[i].connectedTo:
                    if connection not in usedlist:  # appending router to lis for parsing to see if it's connected to router2
                        lis.append(connection)
                        usedlist.append(connection)  # also appending to usedlist so no loops will ensue

            if lis == []:  # if list is empty which means all routers have been checked
                return False

            for router in lis:  # checking all routers in routerpath

                if router == router2:  # if router path found to router2
                    return True

            routers = lis  # changing initial list of routers to the list of routers that were parsed through
            lis = []  # changing lis back to open so new neighbors can be added

    def buildMST(self):

        networklis = list(self.network.vertList.keys())
        temp = networklis[0]  # finding the beginning of the MST, returns string
        start = self.network.getVertex(temp)  # returning Vertex for string found above

        for i in range(len(networklis)):
            self.MST.addVertex(networklis[i])  # getting all vertexes added to MST

        pq = PriorityQueue()

        for v in self.network:  # setting all default values for Prim's algorithm
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in self.network])  # building PQ for Prim

        while not pq.isEmpty():

            currentVert = pq.delMin()  # removing currentVert from list

            for nextVert in currentVert.getConnections():  # checking all connections in nextVert
                newCost = currentVert.getWeight(nextVert)

                if nextVert in pq and newCost < nextVert.getDistance():  # if there's a better option than current
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert, newCost)

        for r in self.network:
            if r.getPred() is not None:  # creating edge values for back and forth along MST
                self.MST.addEdge(r.id, r.getPred().id, r.getDistance())
                self.MST.addEdge(r.getPred().id, r.id, r.getDistance())

    def findPath(self, router1, router2):
        localmst = copy.deepcopy(self.MST)  # making copy of MST to not overwrite anything
        pq = PriorityQueue()

        # if either router does not exist
        if localmst.getVertex(router1) is None or localmst.getVertex(router2) is None:
            return "path not exist"

        localmst.getVertex(router1).setDistance(0)  # setting up all vertices for Dijkstra
        pq.buildHeap([(v.getDistance(), v) for v in localmst])
        nextVert = localmst.getVertex(router1)

        while (not pq.isEmpty()) and (nextVert.id != router2):

            currentVert = pq.delMin()  # removing shortest distance for each vertex in order

            for nextVert in currentVert.getConnections():  # checking for each of its connections
                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)  # adding its theoretical weight

                if newDist < nextVert.getDistance():  # if there is a better path than current
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)

                    if nextVert.id == router2:  # if path is found
                        break

        routerlis = []  # creating variables for router saving and string returning
        pathstr = ""

        if nextVert is None:  # if router2 was not found with connection to router1
            return "path not exist"
        else:
            while True:  # if it was found, breaking each router down and putting into routerlist
                if nextVert.getDistance() == 0:  # if it is the last router in the set
                    routerlis.append(nextVert.id)
                    break
                else:
                    routerlis.append(nextVert.id)
                    nextVert = nextVert.getPred()

        routerlis.reverse()  # initial list is in finish -> start, so changing to start -> finish with .reverse()

        for i in range(len(routerlis)):  # creating pathstr in proper format asked for with routerlist routers
            if i == len(routerlis) - 1:
                pathstr += routerlis[i]  # if router is last, no -> symbol needed
            else:
                pathstr += routerlis[i] + " -> "  # adding -> symbol between routers

        return pathstr  # returning pathstr

    def findForwardingPath(self, router1, router2):
        localnetwork = copy.deepcopy(self.network) # using deepcopy to not overwrite self.network
        pq = PriorityQueue()

        # checking localnetwork to make sure router1 and router2 are real variables
        if localnetwork.getVertex(router1) is None or localnetwork.getVertex(router2) is None:
            return "path not exist"

        localnetwork.getVertex(router1).setDistance(0)  # setting router1 to 0 distance for dijkstra

        pq.buildHeap([(v.getDistance(), v) for v in localnetwork])

        currentVert = localnetwork.getVertex(router1)  # initializing currentVert for whie loop

        while not pq.isEmpty() and currentVert.id != router2:

            currentVert = pq.delMin()  # removing shortest distance for each vertex in order

            for nextVert in currentVert.getConnections():  # checking for each of its connections

                newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)  # adding its theoretical weight

                if newDist < nextVert.getDistance():  # if there is a better path than current
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)

        routerlis = []  # creating variables for router saving and string returning
        pathstr = ""
        dist = currentVert.getDistance()  # getting total distance from router1 -> router2

        if currentVert.id != router2:  # if no path found to router2
            return 'path not exist'
        else:
            while currentVert != localnetwork.getVertex(router1):
                routerlis.append(currentVert.id)
                currentVert = currentVert.getPred()

        routerlis.append(currentVert.id)  # appending start

        routerlis.reverse()  # initial list is in finish -> start, so changing to start -> finish with .reverse()

        for i in range(len(routerlis)):  # creating pathstr in proper format asked for with routerlist routers
            if i == len(routerlis) - 1:
                pathstr += routerlis[i] + " (" + str(dist) + ")"
            else:
                pathstr += routerlis[i] + " -> "  # adding -> symbol between routers

        return pathstr   # returning pathstr

    def findPathMaxWeight(self, router1, router2):
        localnetwork = copy.deepcopy(self.network)
        pq = PriorityQueue()

        # checking localnetwork to make sure router1 and router2 are real variables
        if localnetwork.getVertex(router1) is None or localnetwork.getVertex(router2) is None:
            return "path not exist"

        localnetwork.getVertex(router1).setDistance(0)  # setting router1 to 0 distance for dijkstra

        pq.buildHeap([(v.getDistance(), v) for v in localnetwork])

        currentVert = localnetwork.getVertex(router1)  # initializing currentVert for whie loop

        while not pq.isEmpty() and currentVert.id != router2:

            currentVert = pq.delMin()  # removing shortest distance for each vertex in order

            for nextVert in currentVert.getConnections():  # checking for each of its connections

                newDist = max([currentVert.getDistance() , currentVert.getWeight(nextVert)])
                # changing to only take the max between the two to go with task 6

                if newDist < nextVert.getDistance():  # if there is a better path than current
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)

        routerlis = []  # creating variables for router saving and string returning
        pathstr = ""

        if currentVert.id != router2:  # if no path found to router2
            return 'path not exist'
        else:
            while currentVert != localnetwork.getVertex(
                    router1):  # appending entire path from router1 -> router2 to routerlis
                routerlis.append([currentVert.id, currentVert.getDistance()])
                currentVert = currentVert.getPred()

        routerlis.append([currentVert.id, currentVert.getDistance()])  # appending start

        routerlis.reverse()  # initial list is in finish -> start, so changing to start -> finish with .reverse()

        for i in range(len(routerlis)):  # creating pathstr in proper format asked for with routerlist routers
            if i == len(routerlis) - 1:
                pathstr += routerlis[i][0]
            else:
                pathstr += routerlis[i][0] + " -> "  # adding -> symbol between routers

        return pathstr  # returning pathstr

    @staticmethod
    def nodeEdgeWeight(v):
        return sum([w for w in v.connectedTo.values()])

    @staticmethod
    def totalEdgeWeight(g):
        return sum([ISPNetwork.nodeEdgeWeight(v) for v in g]) // 2


if __name__ == '__main__':
    print("--------- Task1 build graph ---------")
    # Note: You should try all six dataset. This is just a example using 1221.csv
    net = ISPNetwork()
    net.buildGraph('data/3967.csv')

    print("--------- Task2 check if path exists ---------")
    print(net.pathExist("ViennaAustria124", "BerlinGermany161"))
    routers = [v.id for v in random.sample(list(net.network.vertList.values()), 5)]

    for i in range(4):
        print('Router1:', routers[i], ', Router2:', routers[i + 1], 'path exist?:',
              net.pathExist(routers[i], routers[i + 1]))

    print("--------- Task3 build MST ---------")
    net.buildMST()
    print('graph node size', net.MST.numVertices)
    print('graph total edge weights', net.totalEdgeWeight(net.MST))

    print("--------- Task4 find shortest path in MST ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findPath(routers[i], routers[i + 1]))

    '''print("--------- Task5 find shortest path in original graph ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findForwardingPath(routers[i], routers[i + 1]))'''

    print("--------- Task6 find path in LowestMaxWeightFirst algorithm ---------")
    for i in range(4):
        print(routers[i], routers[i + 1], 'Path:', net.findPathMaxWeight(routers[i], routers[i + 1]))

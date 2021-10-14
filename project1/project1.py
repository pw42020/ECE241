"""
UMass ECE 241 - Advanced Programming
Project #1   Fall 2021
project1.py - Sorting and Searching

"""

import matplotlib.pyplot as plt
import sys
import time

"""
Stock class for stock objects
"""
sys.setrecursionlimit(3000)


class Stock:
    """
    Constructor to initialize the stock object
    """

    def __init__(self, sname, symbol, val, prices):  # initializing sname, symbol, val, and prices
        # initializing all variables necessary
        self.sname = sname
        self.symbol = symbol
        self.val = val
        for i in range(len(prices)):
            prices[i] = float(prices[i])
        self.prices = prices

        self.pchange = (float(self.prices[len(self.prices) - 1]) - float(self.prices[1])) / float(self.prices[1])*100

    """
    return the stock information as a string, including name, symbol, 
    market value, and the price on the last day (2021-02-01). 
    For example, the string of the first stock should be returned as: 
    “name: Exxon Mobil Corporation; symbol: XOM; val: 384845.80; price:44.84”. 
    """

    def __str__(self):  # returning string if asked to print Stock
        return "name: " + self.sname + "; symbol: " + self.symbol + "; val: " + str(self.val) + "; price:" + str(self.
                                                                                                                 prices[
                                                                                                                     len(self.prices) - 1])


"""
StockLibrary class to mange stock objects
"""


class StockLibrary:
    """
    Constructor to initialize the StockLibrary
    """

    def __init__(self):  # initializing variables stockList, size, and isSorted
        self.stockList = []
        self.size = len(self.stockList)
        self.isSorted = False
        self.bst = None
        self.BinarySearchTree = AvlTree()

    """
    The loadData method takes the file name of the input dataset,
    and stores the data of stocks into the library. 
    Make sure the order of the stocks is the same as the one in the input file. 
    """

    # function to find longest name
    def findLongestName(self):
        i = 0
        length = 0
        s = None
        for stock in self.stockList:
            if len(stock.sname) > length:
                length = len(stock.sname)  # changing longest name and stock item if length found longer
                print(self.stockList.index(stock))
                s = stock
            i += 1
        return s

    # function to find highest percent change and lowest percent change in the month
    def findpchanges(self):
        high = 0
        highs = None

        low = 0
        lows = None

        for stock in self.stockList:
            if stock.pchange > high:
                high = stock.pchange
                highs = stock
            if stock.pchange < low:
                print(stock,stock.pchange)
                low = stock.pchange
                lows = stock
        print("Highest percent change: ", highs, "at %s" % high)
        print(highs.prices[1],highs.prices[len(highs.prices)-1])
        print("Lowest percent change: ", lows, "at %s" % low)

    def loadData(self, filename: str):  # loading data into stockList from csv

        f = open(filename, "r")  # opening file
        data = f.readlines()  # getting list of all rows

        for i in range(len(data)):
            if i != 0:  # removing first line which is just a key
                company = data[i].split("|")  # splitting line every | to make company a list
                temp = Stock(company[0], company[1], float(company[2]),
                             company[2:])  # creating Stock object with all numbers in
                self.stockList.append(temp)  # adding Stock Object to StockLibrary's stockList

        self.size = len(self.stockList)  # reinitializing size with new value
        self.isSorted = False  # after adding a new Stock, the list will change to an unsorted state, even if it was
        # sorted before

    """
    The linearSearch method searches the stocks based on sname or symbol.
    It takes two arguments as the string for search and an attribute field 
    that we want to search (“name” or “symbol”). 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """

    def linearSearch(self, query: str, attribute: str):  # O(n) search of stockList

        found = False  # will turn to true and leave for loop
        for obj in self.stockList:
            if attribute == "name":  # if searching for a name
                if obj.sname == query:
                    found = True
                    return obj  # returns object if name is found to be the same as searched name

            if attribute == "symbol":  # if searching for symbol
                if obj.symbol == query:
                    found = True
                    return obj  # returns object if symbol is found to be the same as searched symbol
        if not found:  # if object is not found by the end of the for loop
            return "Stock not found"

    """
    Sort the stockList using QuickSort algorithm based on the stock symbol.
    The sorted array should be stored in the same stockList.
    Remember to change the isSorted variable after sorted
    """

    def quickSort(self):

        self.quickSortHelper(self.stockList, 0, len(self.stockList) - 1)

        self.isSorted = True  # changing variable isSorted to True after sorting stockList

    def quickSortHelper(self, alist, first, last):  # implementing quickSortHelper
        if first < last:
            splitpoint = self.partition(alist, first, last)  # calling for partition

            self.quickSortHelper(alist, first, splitpoint - 1)  # reimplementing quickSortHelper with first half list
            self.quickSortHelper(alist, splitpoint + 1, last)  # reimplementing quickSortHelper with second half list

    def partition(self, alist, first, last):  # implementing partition
        pivotvalue = alist[first].symbol

        leftmark = first + 1  # creating leftmark variable
        rightmark = last  # creating rightmark variable

        done = False
        while not done:
            while leftmark <= rightmark and alist[
                leftmark].symbol <= pivotvalue:  # move leftmark up if leftmark < pivot
                leftmark += 1

            while alist[
                rightmark].symbol >= pivotvalue and rightmark >= leftmark:  # move rightmark down if rightmark > pivot
                rightmark -= 1
            if rightmark < leftmark:  # if both points converge
                done = True
            else:
                temp = alist[leftmark]  # swapping points
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    """
    build a balanced BST of the stocks based on the symbol. 
    Store the root of the BST as attribute root, which is a TreeNode type.
    """

    def buildBST(self):  # to build Binary Search Tree
        for i in range(len(self.stockList)):
            self.BinarySearchTree[i] = self.stockList[
                i]  # adding each stock to BinarySearchTree and letting AVLTree handle balance

        self.bst = self.BinarySearchTree.root  # making bst the root of the tree

    """
    Search a stock based on the symbol attribute. 
    It returns the details of the stock as described in __str__() function 
    or a “Stock not found” message when there is no match. 
    """

    def searchBST(self, query, current='dnode'):
        if current == 'dnode':
            return self.searchBST(query,
                                  self.BinarySearchTree.root)  # changing the initial value to the root of the tree
        else:
            if current.payload.symbol == query:  # returning current.val once query is found
                return current.payload
            if current.payload.symbol > query:
                if current.leftChild == None:  # if there are no more children under node in tree
                    return "Stock not found"
                else:
                    return self.searchBST(query,
                                          current.leftChild)  # changing to left child if symbol we're looking for is less than current
            elif current.payload.symbol < query:
                if current.rightChild == None:  # if there are no more children available in tree
                    return "Stock not found"
                else:
                    return self.searchBST(query,
                                          current.rightChild)  # changing to right child if symbol we're looking for is greater than current


# ALL CODE BELOW IS FROM BINARYSEARCHTREEAVL AND AVLTREE FROM PROF. ZINK PER HIS ALLOWANCE
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


class AvlTree(BinarySearchTree):
    '''An extension t the BinarySearchTree data structure which
    strives to keep itself balanced '''

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(
            newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(
            rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


# WRITE YOUR OWN TEST UNDER THIS IF YOU NEED
if __name__ == '__main__':
    stockLib = StockLibrary()
    testSymbol = 'GE'
    testName = 'General Electric Company'

    print("\n-------load dataset-------")
    stockLib.loadData("stock_database.csv")
    print(stockLib.size)
    stock = stockLib.findLongestName()
    stockLib.findpchanges()

    plt.plot(stock.prices[1:])
    plt.title(stock.sname + "'s prices over one month")
    plt.xlabel("Days")
    plt.ylabel("Stock Price (USD)")
    plt.show()

'''
    print("\n-------linear search-------")
    print(stockLib.stockList[99])
    print(stockLib.linearSearch("ACL", "symbol"))
    print(stockLib.linearSearch(testName, "name"))

    print("\n-------quick sort-------")
    print(stockLib.isSorted)
    stockLib.quickSort()
    print(stockLib.isSorted)

    print("\n-------build BST-------")
    stockLib.buildBST()

    print("\n---------search BST---------")
    print(stockLib.searchBST("GOOG"))
'''

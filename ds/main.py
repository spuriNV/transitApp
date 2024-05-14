import uuid
import json
import math
import requests
import pymongo
from pymongo import MongoClient

class Node: 
    def __init__(self, vertex):
        self.vertex = vertex
        self.edge = None
        self.next = None

    def get_vertex(self):
        return self.vertex

    def set_edge(self, edge):
        self.edge = edge
    
    def get_edge(self):
        return self.edge
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

class DisjointSet:
 
    parent = {}

    # perform MakeSet operation
    def makeSet(self, n):
 
        # create `n` disjoint sets (one for each vertex)
        for i in range(n):
            self.parent[i] = i
 
    # Find the root of the set in which element `k` belongs
    def find(self, k):
 
        # if `k` is root
        if self.parent[k] == k:
            return k
 
        # recur for the parent until we find the root
        return self.find(self.parent[k])
 
    # Perform Union of two subsets
    def union(self, a, b):
 
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)
 
        self.parent[x] = y
 

class MinHeap:
  
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0

        rowNum = int(math.log2(maxsize)) + 1
        totalPyramid = (2**(rowNum))-1

        X = Vertex("136c49a9-b952-4034-92ba-49cdd3734c71",  "X", 1, "none", "none")
        newNode = Node(X)
        newEdge = Edges("none", float('inf'), "noEdge")
        newNode.set_edge(newEdge)

        self.Heap = [newNode] * (totalPyramid + 1)
        self.Heap[0] = None
        self.FRONT = 1
  
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
  
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
  
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
  
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size
  
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def get_heap(self):
        return self.Heap
    
    def get_size(self):
        return self.size
    
      # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
        for pos in range(int(self.size/2), 0, -1):
            self.minHeapify(pos)
  
    # Function to heapify the node at pos
    def minHeapify(self, pos):
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if(self.Heap[self.rightChild(pos)] == None):
                if ((self.Heap[pos]).get_edge().get_weight() > (self.Heap[self.leftChild(pos)]).get_edge().get_weight()):
    
                    # Swap with the left child and heapify
                    # the left child
                    if (self.Heap[self.leftChild(pos)]).get_edge().get_weight() < (self.Heap[self.rightChild(pos)]).get_edge().get_weight():
                        self.swap(pos, self.leftChild(pos))
                        self.minHeapify(self.leftChild(pos))
    
            else: 
                if ((self.Heap[pos]).get_edge().get_weight() > (self.Heap[self.leftChild(pos)]).get_edge().get_weight() or 
                (self.Heap[pos]).get_edge().get_weight() > (self.Heap[self.rightChild(pos)]).get_edge().get_weight()):
    
                    # Swap with the left child and heapify
                    # the left child
                    if (self.Heap[self.leftChild(pos)]).get_edge().get_weight() < (self.Heap[self.rightChild(pos)]).get_edge().get_weight():
                        self.swap(pos, self.leftChild(pos))
                        self.minHeapify(self.leftChild(pos))
    
                    # Swap with the right child and heapify
                    # the right child
                    else:
                        self.swap(pos, self.rightChild(pos))
                        self.minHeapify(self.rightChild(pos))
    # Function to insert a node into the heap
    def insert(self, element: Node):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
        temp = self.Heap[self.size]

        self.minHeap()

       # while (temp.get_edge().get_weight() < temp.get_edge().get_weight()):
            #self.swap(current, self.parent(current))
            #current = self.parent(current)

    def searchHeap(self, name):
        for i in range(1, self.size + 1):
            if(name == self.Heap[i].get_vertex().get_name()):
                return i
        return -1
    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, 4):
            printStatement = " PARENT : "+ (self.Heap[i]).get_vertex().get_name() + " " + str((self.Heap[i]).get_edge().get_weight())

            if not self.isLeaf(i):
                if(self.Heap[self.rightChild(i)] == None):
                    printStatement += " LEFT CHILD : " + (self.Heap[2 * i]).get_vertex().get_name() + " " + str((self.Heap[2 * i]).get_edge().get_weight())
                else:
                    printStatement += " LEFT CHILD : " + (self.Heap[2 * i]).get_vertex().get_name() + " " + str((self.Heap[2 * i]).get_edge().get_weight()) + " RIGHT CHILD : "+ (self.Heap[2 * i + 1]).get_vertex().get_name() + " " + str((self.Heap[2 * i + 1]).get_edge().get_weight())
            
            print(printStatement)

  
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
 
class Vertex:

    def __init__(self, id : uuid.uuid4(), name : str, stop_id1 : int, stop_id2 : int, line_num : str, mode : str):
        self.id = id; 
        self.name = name
        self.stop_id1 = stop_id1
        self.stop_id2 = stop_id2
        self.line_num = line_num
        self.mode = mode


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
  
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_stopId1(self):
        return self.stop_id1

    def set_stopId1(self, stop_id):
        self.stop_id1 = stop_id1
    
    def get_stopId2(self):
        return self.stop_id2

    def set_stopId2(self, stop_id):
        self.stop_id2 = stop_id2

    def get_line_num(self):
        return self.line_num

    def set_line_num(self, line_num):
        self.line_num = line_num
    
    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode

    
class Edges: 

    def __init__(self, line : str):
        self.line = line 
        self.weight = -1
        self.name = ""

    def __init__(self, line : str, weight : int, name : str):
        self.line = line 
        self.weight = weight 
        self.name = name

    def operator(self, weight):
        return self.weight < weight
  
    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_line(self):
        return self.line

    def set_line(self, line):
        self.line = line 
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name



# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, vertices, n):
        self.graph = [None] * n

        for i in range(n):
            node = Node(vertices[i])
            newEdge = Edges("none", 0, "noEdge")
            node.set_edge(newEdge)    
            self.graph[i] = node
 
    def add_edge(self, sourceNum, vertex, edge):
        
        temp = self.graph[sourceNum]

        while(temp.next != None):
            temp = temp.next

        node = Node(vertex)
        node.set_edge(edge)
        temp.next = node
    

    def dijkstra(self, start, finish):

        # chart is going to be a dictionary with vertices, value of edge, and previous vertex 
        # chart contains vertex, visited value, edge number value, and previous vertex
        # self.graph is needed for the adjacency list 
        
        # 1) set starting vertex to distance 0, 

        # 2) for the current node calculate the distance to all unvisited neigbours
            # 2.1) update shortest distance, if new distance is shorter than old distance and previous node

            # so traverse adj list find neighbours of current node and their edges
            # and in the chart update previous node and shortest distance if new distance is shorter than old
        
        chart = {}
        for i in range(len(self.graph)):
            chart[self.graph[i].get_vertex().get_name()] = [False, float('inf'), None]
        
        chart[start][1] = 0

        min = 1000
        chabee = 'default'
        counter = 0
        allNotVisited = True

        while allNotVisited:
            for key in chart: 
                if chart[key][1] < min and chart[key][0] == False: 
                    min = chart[key][1]
                    chabee = key

            for i in range (len(self.graph)):
                if (self.graph[i].get_vertex().get_name() == chabee):
                    counter = i
                    break

            head = self.graph[counter]    
            temp = head
            tempNext = temp.get_next()
            
            while(tempNext != None):
                neighbour_name = tempNext.get_vertex().get_name()
                neighbour_edge = tempNext.get_edge().get_weight()

                curr_edge = chart[chabee][1]

                if(curr_edge + neighbour_edge < chart[neighbour_name][1] and chart[neighbour_name][0] == False): 
                    chart[neighbour_name][1] = curr_edge + neighbour_edge
                    chart[neighbour_name][2] = chabee  

                tempNext = tempNext.get_next()

            # 3) mark current node as visited
            chart[chabee][0] = True
            min = 1000

            allNotVisited = False
            for key in chart:
                if chart[key][0] == False: 
                    allNotVisited = True 

        # now get shortest path from two points
           
        finalNum = chart[finish][1]
        path = []
        while(finish != None):
            path.append(finish)
            finish = chart[finish][2]
        
        return finalNum, path


    # space complexity: O(E + V), tine complexity: O(E log(V))
    def prims(self, start):

        # min-heap with edges and vertices, self.heap stores vertices and indices, adjacency list, seperate dictionary to store vertex and the preceding edge

        # 1) set starting node's value to 0, and everythibg else to infinity in the map
        # 2) extract min from heap and explore its edges that are connected to vertices in the heap
        # 3) for each neighbour, update its value in the heap (if the heap value is larger), and update the seperate dictionary

        minheap = MinHeap(len(self.graph))

        veDict = {}

        #filling minheap with vertex and value
        for i in range(len(self.graph)):
            temp = self.graph[i]
            newEdge = Edges("none", float('inf'), "noEdge")
            temp.set_edge(newEdge)
            minheap.insert(temp)
        
        #setting starting vertex's value to 0 in minheap
        heap = minheap.get_heap()
        indec = -1
        for i in range(1, minheap.get_size() + 1):
            if(start == heap[i].get_vertex().get_name()):
               indec = i

        heap[indec].get_edge().set_weight(0)

        # extract min 
        while(minheap.get_size() != 0):
            minheap.minHeap()
            minNode = minheap.remove()
            # print(minNode.get_vertex().get_name())

            indexGraph = -1 
            for i in range(len(self.graph)):
                if(minNode.get_vertex().get_name() == self.graph[i].get_vertex().get_name()):
                        indexGraph = i

                # explore neighbours
            head = self.graph[indexGraph]
            temp = head.get_next()

            while(temp != None):
                
                    # check if neighbiour exists in heap 
                    # if so: 
                            # record in veDict() and update heap value if it the heap value is bigger

                index = minheap.searchHeap(temp.get_vertex().get_name())

                if(index != -1): 
                    if(temp.get_edge().get_weight() < heap[index].get_edge().get_weight()):
                        veDict[heap[index].get_vertex().get_name()] = temp.get_edge().get_name() 
                        heap[index].get_edge().set_weight(temp.get_edge().get_weight())

                temp = temp.get_next()

        # see list of edges in spanning tree 

        return len(veDict), veDict
    
    def findArticulationPoints(self, startVertex):
        time = 0
        visited = []
        ap = []
        visitedTime = {}
        lowTime = {}
        parent = {startVertex.get_name():"empty"}
        vertex = startVertex

        self.dfs(vertex, time, visited, ap, visitedTime, lowTime, parent)
        return ap


    def dfs(self, vertex, time, visited, ap, visitedTime, lowTime, parent):
        start = vertex
        visited.append(start.get_name())
        visitedTime[start.get_name()] = time
        lowTime[start.get_name()] = time
        time = time + 1

        childCount = 0 
        isArticulationPoint = False 

        indec = 0
        for i in range(0, len(self.graph)):
            if(start.get_name() == self.graph[i].get_vertex().get_name()):
               indec = i
    
        head = self.graph[indec]
        temp = head.get_next()

        while(temp != None):
            if(temp.get_vertex().get_name() != parent[start.get_name()]):
                if(temp.get_vertex().get_name() not in visited):
                    parent[temp.get_vertex().get_name()] = start.get_name()
                    childCount = childCount + 1
                    self.dfs(temp.get_vertex(), time, visited, ap, visitedTime, lowTime, parent)

                    if(visitedTime[start.get_name()] <= lowTime[temp.get_vertex().get_name()]):
                        isArticulationPoint = True

                    else:
                        lowTime[start.get_name()] = min(lowTime[start.get_name()], lowTime[temp.get_vertex().get_name()])
                    
                else:
                    lowTime[start.get_name()] = min(lowTime[start.get_name()], visitedTime[temp.get_vertex().get_name()])

            temp = temp.get_next()


        if((parent[start.get_name()] == "empty" and childCount >= 2) or (parent[start.get_name()] != "empty" and isArticulationPoint == True)):
            ap.append(start.get_name())


        # book keeping: 
            # visited sets in dfs traversal 
            # time, current visited time
            # set of AP 
            # 1. visited time of vertex map 
            # 2. low time of vertex (min of visited time of all edges and vertcies which are reachable from given vertex)
            # 3. parent of a given vertex in the dfs traversal


        # 2 criteria of AP: 
            # 1. root vertex of two independent children 
            # 2. visited time <= lowtime of adj vertices

    def findCycle(self):
 
        # initialize `DisjointSet` class
        ds = DisjointSet()
    
        # create a singleton set for each element of the universe
        n = len(self.graph)
        ds.makeSet(n)
        # this is O(V)
    
        # consider every edge (u, v)
        for u in range(n):
    
            # Recur for all adjacent vertices
            temp = self.graph[u]
            while temp != None:
    
                v = 0
                for i in range(0, len(self.graph)):
                    if (temp.get_vertex().get_name() == self.graph[i].get_vertex().get_name()):
                        v = i
                
                if u != v:
                    # find the root of the sets to which elements `u` and `v` belongs
                    x = ds.find(u)
                    y = ds.find(v)
        
                    # if both `u` and `v` have the same parent, the cycle is found
                    if x == y:
                        return True
                    else:
                        ds.union(x, y)

                temp = temp.get_next()
        return False

    def printAdjList(self):
        num = 0
        for i in range (0, len(self.graph)):
            temp = self.graph[i]
            result = str(num) + " " + self.graph[i].get_vertex().get_name()
            while(temp.next != None):
                result += " - " + "(" + temp.get_next().get_vertex().get_name() + ", " + str(temp.get_next().get_edge().get_weight()) + ", " + temp.get_next().get_edge().get_line() + ")"
                temp = temp.next
            print(result)  
            num = num + 1



#--------------------------------------------------------------

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/') 
db = client['transit'] 
collection = db['stops_collection']  

# Fetch data from MongoDB
cursor = collection.find()

# Define the filename
filename = 'transit.json'

# Open the file in write mode
with open(filename, 'w') as file:
    # Iterate over the cursor and write each document as JSON to the file
    for document in cursor:
        file.write(json.dumps(document, indent=4))
        file.write('\n')  # Add a newline between documents

# Close the connection
client.close()


# read file
with open('transit.json', 'r') as myfile:
    data=myfile.read()

client = pymongo.MongoClient("mongodb://localhost:27017")

# parse file
obj = json.loads(data)
vertices = []
for i in range(len(obj)):

    vertex = Vertex(str(obj[i]["id"]), str(obj[i]["stop_name"]), str(obj[i]["stop_id1"]), str(obj[i]["stop_id2"]), str(obj[i]["line_number"]), str(obj[i]["mode_type"]))
    vertices.append(vertex)

  # Edge (x, y, w) represents an edge from `x` to `y` having weight `w` // first section is millenium line


graph = Graph(vertices, len(obj))


#--------------------------------------------------------------

#millenium line   

for i in range(0, 3):
    varName = "edge" + str(i) + "_" + str(i+1)
    paraName = str(obj[i]["stop_name"]) + "(" + str(i) + ")" + "_" + str(obj[i+1]["stop_name"] + "(" + str(i+1) + ")")
    varName = Edges("millenium", 10, paraName)

edge0_1 = Edges("millenium", 2, str(obj[0]["stop_name"]) + "(" + str(0) + ")" + "_" + str(obj[1]["stop_name"] + "(" + str(1) + ")")) #  (vertices[0], vcc-clark) - (vertices[1], commercial-broadway) 
edge1_2 = Edges("millenium", 3, str(obj[1]["stop_name"]) + "(" + str(1) + ")" + "_" + str(obj[2]["stop_name"] + "(" + str(2) + ")")) #  (vertices[1], commercial-broadway) - (vertices[2], renfrew) 
edge2_3 = Edges("millenium", 1, str(obj[2]["stop_name"]) + "(" + str(2) + ")" + "_" + str(obj[3]["stop_name"] + "(" + str(3) + ")"))#  (vertices[2], renfrew) - (vertices[3], rupert) 

graph.add_edge(0, vertices[1], edge0_1)
graph.add_edge(1, vertices[0], edge0_1)

graph.add_edge(1, vertices[2], edge1_2)
graph.add_edge(2, vertices[1], edge1_2)

graph.add_edge(2, vertices[3], edge2_3)
graph.add_edge(3, vertices[2], edge2_3)


#--------------------------------------------------------------

# canada line

edge4_5 = Edges("canada", 3, str(obj[4]["stop_name"]) + "(" + str(4) + ")" + "_" + str(obj[5]["stop_name"] + "(" + str(5) + ")")) #  (vertices[17], waterfront) - (vertices[18], vancouver city centre) 
edge5_6 = Edges("canada", 2, str(obj[5]["stop_name"]) + "(" + str(5) + ")" + "_" + str(obj[6]["stop_name"] + "(" + str(6) + ")")) #  (vertices[18], vancouver city centre) - (vertices[19], yaletown-roundhouse) 
edge6_7 = Edges("canada", 2, str(obj[6]["stop_name"]) + "(" + str(6) + ")" + "_" + str(obj[7]["stop_name"] + "(" + str(7) + ")")) #  (vertices[19], yaletown-roundhouse) - (vertices[20], olympic village) 
edge7_8 = Edges("canada", 2, str(obj[7]["stop_name"]) + "(" + str(7) + ")" + "_" + str(obj[8]["stop_name"] + "(" + str(8) + ")")) #  (vertices[20], olympic village) - (vertices[21], broadway-city hall) 
edge8_9 = Edges("canada", 2, str(obj[8]["stop_name"]) + "(" + str(8) + ")" + "_" + str(obj[9]["stop_name"] + "(" + str(9) + ")"))#  (vertices[21], broadway-city hall) - (vertices[22], king edward) 
edge9_10 = Edges("canada", 3, str(obj[9]["stop_name"]) + "(" + str(9) + ")" + "_" + str(obj[10]["stop_name"] + "(" + str(10) + ")")) #  (vertices[22], king edward) - (vertices[23], oakridge-41st) 
edge10_11 = Edges("canada", 2, str(obj[10]["stop_name"]) + "(" + str(10) + ")" + "_" + str(obj[11]["stop_name"] + "(" + str(11) + ")"))#  (vertices[23], oakridge-41st) - (vertices[24], langara-49th) 
edge11_12 = Edges("canada", 3, str(obj[11]["stop_name"]) + "(" + str(11) + ")" + "_" + str(obj[12]["stop_name"] + "(" + str(12) + ")")) #  (vertices[24], langara-49th) - (vertices[25], marine drive) 

graph.add_edge(4, vertices[5], edge4_5)
graph.add_edge(5, vertices[4], edge4_5)

graph.add_edge(5, vertices[6], edge5_6)
graph.add_edge(6, vertices[5], edge5_6)

graph.add_edge(6, vertices[7], edge6_7)
graph.add_edge(7, vertices[6], edge6_7)

graph.add_edge(7, vertices[8], edge7_8)
graph.add_edge(8, vertices[7], edge7_8)

graph.add_edge(8, vertices[9], edge8_9)
graph.add_edge(9, vertices[8], edge8_9)

graph.add_edge(9, vertices[10], edge9_10)
graph.add_edge(10, vertices[9], edge9_10)

graph.add_edge(10, vertices[11], edge10_11)
graph.add_edge(11, vertices[10], edge10_11)

graph.add_edge(11, vertices[12], edge11_12)
graph.add_edge(12, vertices[11], edge11_12)


#--------------------------------------------------------------

# expo line

edge4_13 = Edges("expo", 3, str(obj[4]["stop_name"]) + "(" + str(4) + ")" + "_" + str(obj[13]["stop_name"]) + "(" + str(13) + ")")
edge13_14 = Edges("expo", 1, str(obj[13]["stop_name"]) + "(" + str(13) + ")" + "_" + str(obj[14]["stop_name"]) + "(" + str(14) + ")") #  (vertices[33], burrard) - (vertices[34], granville) 
edge14_15 = Edges("expo", 2, str(obj[14]["stop_name"]) + "(" + str(14) + ")" + "_" + str(obj[15]["stop_name"]) + "(" + str(15) + ")") #  (vertices[34], granville) - (vertices[35], stadium-chinatown) 
edge15_16 = Edges("expo", 2, str(obj[15]["stop_name"]) + "(" + str(15) + ")" + "_" + str(obj[16]["stop_name"]) + "(" + str(16) + ")") #  (vertices[35], stadium-chinatown) - (vertices[36], main street-science world) 
edge16_1 = Edges("expo", 3, str(obj[16]["stop_name"]) + "(" + str(16) + ")" + "_" + str(obj[1]["stop_name"]) + "(" + str(1) + ")") #  (vertices[36], main street-science world) - (vertices[1], commercial-broadway) 
edge1_17 = Edges("expo", 3, str(obj[1]["stop_name"]) + "(" + str(1) + ")" + "_" + str(obj[17]["stop_name"]) + "(" + str(17) + ")") #  (vertices[1], commercial-broadway) - (vertices[37], nanaimo) 
edge17_18 = Edges("expo", 1, str(obj[17]["stop_name"]) + "(" + str(17) + ")" + "_" + str(obj[18]["stop_name"]) + "(" + str(18) + ")") #  (vertices[37], nanaimo) - (vertices[38], 29th avenue) 
edge18_19 = Edges("expo", 2, str(obj[18]["stop_name"]) + "(" + str(18) + ")" + "_" + str(obj[19]["stop_name"]) + "(" + str(19) + ")") #  (vertices[38], 29th avenue) - (vertices[39], joyce-collingwood) 


graph.add_edge(4, vertices[13], edge4_13)
graph.add_edge(13, vertices[4], edge4_13)

graph.add_edge(13, vertices[14], edge13_14)
graph.add_edge(14, vertices[13], edge13_14)

graph.add_edge(14, vertices[15], edge14_15)
graph.add_edge(15, vertices[14], edge14_15)

graph.add_edge(15, vertices[16], edge15_16)
graph.add_edge(16, vertices[15], edge15_16)

graph.add_edge(16, vertices[1], edge16_1)
graph.add_edge(1, vertices[16], edge16_1)

graph.add_edge(1, vertices[17], edge1_17)
graph.add_edge(17, vertices[1], edge1_17)

graph.add_edge(17, vertices[18], edge17_18)
graph.add_edge(18, vertices[17], edge17_18)

graph.add_edge(18, vertices[19], edge18_19)
graph.add_edge(19, vertices[18], edge18_19)

#--------------------------------------------------------------

# 99 bus 

# starts with commerical broadway, then broadway-city hall, then ubc exchange

edge1_21 = Edges("99", 10, str(obj[1]["stop_name"]) + "(" + str(1) + ")" + "_" + str(obj[21]["stop_name"] + "(" + str(21) + ")"))
edge21_22 = Edges("99", 10, str(obj[21]["stop_name"]) + "(" + str(21) + ")" + "_" + str(obj[22]["stop_name"]) + "(" + str(22) + ")")
edge22_23 = Edges("99", 10, str(obj[22]["stop_name"]) + "(" + str(22) + ")" + "_" + str(obj[23]["stop_name"]) + "(" + str(23) + ")")
edge23_24 = Edges("99", 10, str(obj[23]["stop_name"]) + "(" + str(23) + ")" + "_" + str(obj[24]["stop_name"]) + "(" + str(24) + ")")
edge24_8 = Edges("99", 10, str(obj[24]["stop_name"]) + "(" + str(24) + ")" + "_" + str(obj[8]["stop_name"]) + "(" + str(8) + ")")
edge8_25 = Edges("99", 10, str(obj[8]["stop_name"]) + "(" + str(8) + ")" + "_" + str(obj[25]["stop_name"]) + "(" + str(25) + ")")
edge25_26 = Edges("99", 10, str(obj[25]["stop_name"]) + "(" + str(25) + ")" + "_" + str(obj[26]["stop_name"]) + "(" + str(26) + ")")
edge26_27 = Edges("99", 10, str(obj[26]["stop_name"]) + "(" + str(26) + ")" + "_" + str(obj[27]["stop_name"]) + "(" + str(27) + ")")
edge27_28 = Edges("99", 10, str(obj[27]["stop_name"]) + "(" + str(27) + ")" + "_" + str(obj[28]["stop_name"]) + "(" + str(28) + ")")
edge28_29 = Edges("99", 10, str(obj[28]["stop_name"]) + "(" + str(28) + ")" + "_" + str(obj[29]["stop_name"]) + "(" + str(29) + ")")
edge29_30 = Edges("99", 10, str(obj[29]["stop_name"]) + "(" + str(29) + ")" + "_" + str(obj[30]["stop_name"]) + "(" + str(30) + ")")
edge30_20 = Edges("99", 10, str(obj[30]["stop_name"]) + "(" + str(30) + ")" + "_" + str(obj[20]["stop_name"]) + "(" + str(20) + ")")


graph.add_edge(1, vertices[21], edge1_21)
graph.add_edge(21, vertices[1], edge1_21)

graph.add_edge(21, vertices[22], edge21_22)
graph.add_edge(22, vertices[21], edge21_22)

graph.add_edge(22, vertices[23], edge22_23)
graph.add_edge(23, vertices[22], edge22_23)

graph.add_edge(23, vertices[24], edge23_24)
graph.add_edge(24, vertices[23], edge23_24)

graph.add_edge(24, vertices[8], edge24_8)
graph.add_edge(8, vertices[24], edge24_8)

graph.add_edge(8, vertices[25], edge8_25)
graph.add_edge(25, vertices[8], edge8_25)

graph.add_edge(25, vertices[26], edge25_26)
graph.add_edge(26, vertices[25], edge25_26)

graph.add_edge(26, vertices[27], edge26_27)
graph.add_edge(27, vertices[26], edge26_27)

graph.add_edge(27, vertices[28], edge27_28)
graph.add_edge(28, vertices[27], edge27_28)

graph.add_edge(28, vertices[29], edge28_29)
graph.add_edge(29, vertices[28], edge28_29)

graph.add_edge(29, vertices[30], edge29_30)
graph.add_edge(30, vertices[29], edge29_30)

graph.add_edge(30, vertices[20], edge30_20)
graph.add_edge(20, vertices[30], edge30_20)


#--------------------------------------------------------------

# R4 bus
edge19_31 = Edges("R4", 10, str(obj[19]["stop_name"]) + "(" + str(19) + ")" + "_" + str(obj[31]["stop_name"]) + "(" + str(31) + ")")
edge31_32 = Edges("R4", 10, str(obj[31]["stop_name"]) + "(" + str(31) + ")" + "_" + str(obj[32]["stop_name"]) + "(" + str(32) + ")")
edge32_33 = Edges("R4", 10, str(obj[32]["stop_name"]) + "(" + str(32) + ")" + "_" + str(obj[33]["stop_name"]) + "(" + str(33) + ")")
edge33_34 = Edges("R4", 10, str(obj[33]["stop_name"]) + "(" + str(33) + ")" + "_" + str(obj[34]["stop_name"]) + "(" + str(34) + ")")
edge34_35 = Edges("R4", 10, str(obj[34]["stop_name"]) + "(" + str(34) + ")" + "_" + str(obj[35]["stop_name"]) + "(" + str(35) + ")")
edge35_36 = Edges("R4", 10, str(obj[35]["stop_name"]) + "(" + str(35) + ")" + "_" + str(obj[36]["stop_name"]) + "(" + str(36) + ")")
edge36_37 = Edges("R4", 10, str(obj[36]["stop_name"]) + "(" + str(36) + ")" + "_" + str(obj[37]["stop_name"]) + "(" + str(37) + ")")
edge37_38 = Edges("R4", 10, str(obj[37]["stop_name"]) + "(" + str(37) + ")" + "_" + str(obj[38]["stop_name"]) + "(" + str(38) + ")")
edge38_10 = Edges("R4", 10, str(obj[38]["stop_name"]) + "(" + str(38) + ")" + "_" + str(obj[10]["stop_name"]) + "(" + str(10) + ")")
edge10_39 = Edges("R4", 10, str(obj[10]["stop_name"]) + "(" + str(10) + ")" + "_" + str(obj[39]["stop_name"]) + "(" + str(39) + ")")
edge39_40 = Edges("R4", 10, str(obj[39]["stop_name"]) + "(" + str(39) + ")" + "_" + str(obj[40]["stop_name"]) + "(" + str(40) + ")")
edge40_41 = Edges("R4", 10, str(obj[40]["stop_name"]) + "(" + str(40) + ")" + "_" + str(obj[41]["stop_name"]) + "(" + str(41) + ")")
edge41_42 = Edges("R4", 10, str(obj[41]["stop_name"]) + "(" + str(41) + ")" + "_" + str(obj[42]["stop_name"]) + "(" + str(42) + ")")
edge42_43 = Edges("R4", 10, str(obj[42]["stop_name"]) + "(" + str(42) + ")" + "_" + str(obj[43]["stop_name"]) + "(" + str(43) + ")")
edge43_44 = Edges("R4", 10, str(obj[43]["stop_name"]) + "(" + str(43) + ")" + "_" + str(obj[44]["stop_name"]) + "(" + str(44) + ")")
edge44_20 = Edges("R4", 10, str(obj[44]["stop_name"]) + "(" + str(44) + ")" + "_" + str(obj[20]["stop_name"]) + "(" + str(20) + ")")

graph.add_edge(19, vertices[31], edge19_31)
graph.add_edge(31, vertices[19], edge19_31)

graph.add_edge(31, vertices[32], edge31_32)
graph.add_edge(32, vertices[31], edge31_32)

graph.add_edge(32, vertices[33], edge32_33)
graph.add_edge(33, vertices[32], edge32_33)

graph.add_edge(33, vertices[34], edge33_34)
graph.add_edge(34, vertices[33], edge33_34)

graph.add_edge(34, vertices[35], edge34_35)
graph.add_edge(35, vertices[34], edge34_35)

graph.add_edge(35, vertices[36], edge35_36)
graph.add_edge(36, vertices[35], edge35_36)

graph.add_edge(36, vertices[37], edge36_37)
graph.add_edge(37, vertices[36], edge36_37)

graph.add_edge(37, vertices[38], edge37_38)
graph.add_edge(38, vertices[37], edge37_38)

graph.add_edge(38, vertices[10], edge38_10)
graph.add_edge(10, vertices[38], edge38_10)

graph.add_edge(10, vertices[39], edge10_39)
graph.add_edge(39, vertices[10], edge10_39)

graph.add_edge(39, vertices[40], edge39_40)
graph.add_edge(40, vertices[39], edge39_40)

graph.add_edge(40, vertices[41], edge40_41)
graph.add_edge(41, vertices[40], edge40_41)

graph.add_edge(41, vertices[42], edge41_42)
graph.add_edge(42, vertices[41], edge41_42)

graph.add_edge(42, vertices[43], edge42_43)
graph.add_edge(43, vertices[42], edge42_43)

graph.add_edge(43, vertices[44], edge43_44)
graph.add_edge(44, vertices[43], edge43_44)

graph.add_edge(44, vertices[20], edge44_20)
graph.add_edge(20, vertices[44], edge44_20)

# starts with joyce collingwood, then oakrdige, then ubc


#--------------------------------------------------------------

# R5 bus

edge45_46 = Edges("R5", 10, str(obj[45]["stop_name"]) + "(" + str(45) + ")" + "_" + str(obj[46]["stop_name"]) + "(" + str(46) + ")")
edge46_47 = Edges("R5", 10, str(obj[46]["stop_name"]) + "(" + str(46) + ")" + "_" + str(obj[47]["stop_name"]) + "(" + str(47) + ")")
edge47_48 = Edges("R4", 10, str(obj[47]["stop_name"]) + "(" + str(47) + ")" + "_" + str(obj[48]["stop_name"]) + "(" + str(48) + ")")
edge48_49 = Edges("R5", 10, str(obj[48]["stop_name"]) + "(" + str(48) + ")" + "_" + str(obj[49]["stop_name"]) + "(" + str(49) + ")")
edge49_50 = Edges("R5", 10, str(obj[49]["stop_name"]) + "(" + str(49) + ")" + "_" + str(obj[50]["stop_name"]) + "(" + str(50) + ")")
edge50_51 = Edges("R5", 10, str(obj[50]["stop_name"]) + "(" + str(50) + ")" + "_" + str(obj[51]["stop_name"]) + "(" + str(51) + ")")
edge51_13 = Edges("R5", 10, str(obj[51]["stop_name"]) + "(" + str(51) + ")" + "_" + str(obj[13]["stop_name"]) + "(" + str(13) + ")")

graph.add_edge(45, vertices[46], edge45_46)
graph.add_edge(46, vertices[45], edge45_46)

graph.add_edge(46, vertices[47], edge46_47)
graph.add_edge(47, vertices[46], edge46_47)

graph.add_edge(47, vertices[48], edge47_48)
graph.add_edge(48, vertices[47], edge47_48)

graph.add_edge(48, vertices[49], edge48_49)
graph.add_edge(49, vertices[48], edge48_49)

graph.add_edge(49, vertices[50], edge49_50)
graph.add_edge(50, vertices[49], edge49_50)

graph.add_edge(50, vertices[51], edge50_51)
graph.add_edge(51, vertices[50], edge50_51)

graph.add_edge(51, vertices[13], edge51_13)
graph.add_edge(13, vertices[51], edge51_13)


# have the whole line plus burrard station

#--------------------------------------------------------------

print("\n")
print("This is the Vancouver Rapid Transit Network Analysis")
print("\n")
print("Type 'D' - Djikstra's (with linked lists): ")
print("Type 'P' - Prim's (with Minheap): ")
print("Type 'A' - Articualtion Points (with DFS): ")
print("Type 'C' - CycleExists (with Disjoint Sets)")
print("\n")
value = input("Type here: ")

if value == "D": 
    print("To run Djikstra's algorithm, you must input two values: ")
    print("\n")
    startingValue = input("Type the name of the starting vertex: ")
    finalValue = input("Type the name of the ending vertex: ")
    print("\n")

     # find index associated with name
    
    indec = 0
    extraTime = 0
    for i in range(0, len(graph.graph)):
        if(startingValue == graph.graph[i].get_vertex().get_name()):
            indec = i
    
    # If the object has a stopid1 or stopid2 not equal to 0, ask if east or west? 

    if(graph.graph[indec].get_vertex().get_stopId1() != 0 or graph.graph[indec].get_vertex().get_stopId2 != 0):
        eastOrWest = input("Are you going east or west? Type 'E' or 'W': ")

        # call to translink api to determine the expected time of bus arrival
        stopidValue = 0
        apiKeyValue = ''
        headers = {'Accept': 'application/json'}
        busNum = graph.graph[indec].get_vertex().get_line_num()
        if(eastOrWest == "W"):
            stopidValue = graph.graph[indec].get_vertex().get_stopId1()
            response = requests.get('https://api.translink.ca/rttiapi/v1/stops/'+ str(stopidValue) + '/estimates?apikey=' + apiKeyValue + '&count=3&timeframe=240&routeNo=' + str(busNum), headers=headers)
            extraTime = response.json()[0]["Schedules"][0]["ExpectedCountdown"]
        elif(eastOrWest == "E"):
            stopidValue = graph.graph[indec].get_vertex().get_stopId2()
            response = requests.get('https://api.translink.ca/rttiapi/v1/stops/'+ str(stopidValue) + '/estimates?apikey=' + apiKeyValue + '&count=3&timeframe=240&routeNo=' + str(busNum), headers=headers)
            extraTime = response.json()[0]["Schedules"][0]["ExpectedCountdown"]
        else:
            print("Not a valid input.")
       
    print("The shortest time is: " + str(graph.dijkstra(startingValue, finalValue)[0]) + " + " + str(extraTime) + " minutes.")
    print("The stops involved are: ")
    print(graph.dijkstra(startingValue, finalValue)[1])

elif value == "P": 
    print("To run Prim's algorithm, you must input one value: ")
    print("\n")
    startingValue = input("Type the name of the starting vertex: ")
    print("The number of edges in the minimum spanning tree is " + str(graph.prims(startingValue)[0]) + " out of 54")
    print("The edges involved are: ")
    print(graph.prims(startingValue)[1])

elif value == "A": 
    print("To run Articulation Points algorithm, you must input one value: ")
    print("\n")
    startingValue = input("Type the name of the starting vertex: ")
    print("The number of articulation points are " + srt(graph.findArticulationPoints(startingValue)[0]))
    print("The articulation points are: ")
    print(graph.findArticulationPoints(startingValue)[1])

elif value == "C": 
    print("This will run the Cycle Exists algorithm")
    if graph.findCycle() == True:
        print("The graph has a cycle.")
    elif graph.findCycle() == False: 
        print("The graph does not have a cycle.")

else: 
    print("That is not a valid input")


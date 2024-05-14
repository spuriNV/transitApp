import pytest
import main as main
from main import Graph
from main import Vertex 
from main import Edges 
from main import Node

# pytest graph_test.py

def test_dijkstra():

    A = Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train")
    B = Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train")
    C = Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train")
    D = Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train")
    E = Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train")
    F = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train")

    vertices = []
    vertices.append(A)
    vertices.append(B)
    vertices.append(C)
    vertices.append(D)
    vertices.append(E)
    vertices.append(F)

    this_graph = Graph(vertices, 6)

    edgeAB = Edges("line", 2, "edgeAB")
    edgeAD = Edges("line", 8, "edgeAD")
    edgeBD = Edges("line", 5, "edgeBD")
    edgeBE = Edges("line", 6, "edgeBE")
    edgeDF = Edges("line", 2, "edgeDF")
    edgeDE = Edges("line", 3, "edgeDE")
    edgeEF = Edges("line", 1, "edgeEF")
    edgeFC = Edges("line", 3, "edgeFC")
    edgeEC = Edges("line", 9, "edgeEC")

    this_graph.add_edge(0, B, edgeAB)
    this_graph.add_edge(0, D, edgeAD)
        
    this_graph.add_edge(1, A, edgeAB)
    this_graph.add_edge(1, D, edgeBD)
    this_graph.add_edge(1, E, edgeBE)

    this_graph.add_edge(2, E, edgeEC)
    this_graph.add_edge(2, F, edgeFC)

    this_graph.add_edge(3, A, edgeAD)
    this_graph.add_edge(3, B, edgeBD)
    this_graph.add_edge(3, E, edgeDE)
    this_graph.add_edge(3, F, edgeDF)

    this_graph.add_edge(4, B, edgeBE)
    this_graph.add_edge(4, C, edgeEC)
    this_graph.add_edge(4, D, edgeDE)
    this_graph.add_edge(4, F, edgeEF)

    this_graph.add_edge(5, C, edgeFC)
    this_graph.add_edge(5, D, edgeDF)
    this_graph.add_edge(5, E, edgeEF)

    assert this_graph.dijkstra(this_graph.graph[0].get_vertex().get_name(), this_graph.graph[2].get_vertex().get_name()) == ['C', 'F', 'D', 'B', 'A']

def test_prims():

    A = Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train")
    B = Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train")
    C = Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train")
    D = Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train")
    E = Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train")
    F = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train")

    vertices = []
    vertices.append(A)
    vertices.append(B)
    vertices.append(C)
    vertices.append(D)
    vertices.append(E)
    vertices.append(F)

    this_graph = Graph(vertices, 6)

    edgeAB = Edges("line", 3, "edgeAB")
    edgeAD = Edges("line", 1, "edgeAD")
    edgeBD = Edges("line", 3, "edgeBD")
    edgeCD = Edges("line", 1, "edgeCD")
    edgeBC = Edges("line", 1, "edgeBC")

    edgeDE = Edges("line", 6, "edgeDE")
    edgeEF = Edges("line", 2, "edgeEF")
    edgeFC = Edges("line", 4, "edgeFC")
    edgeEC = Edges("line", 5, "edgeEC")

    this_graph.add_edge(0, B, edgeAB)
    this_graph.add_edge(0, D, edgeAD)
        
    this_graph.add_edge(1, A, edgeAB)
    this_graph.add_edge(1, D, edgeBD)
    this_graph.add_edge(1, C, edgeBC)

    this_graph.add_edge(2, B, edgeBC)
    this_graph.add_edge(2, D, edgeCD)
    this_graph.add_edge(2, E, edgeEC)
    this_graph.add_edge(2, F, edgeFC)

    this_graph.add_edge(3, A, edgeAD)
    this_graph.add_edge(3, B, edgeBD)
    this_graph.add_edge(3, E, edgeDE)
    this_graph.add_edge(3, C, edgeCD)

    this_graph.add_edge(4, C, edgeEC)
    this_graph.add_edge(4, D, edgeDE)
    this_graph.add_edge(4, F, edgeEF)

    this_graph.add_edge(5, C, edgeFC)
    this_graph.add_edge(5, E, edgeEF)

    assert this_graph.prims(this_graph.graph[0].get_vertex()) == {'B': 'edgeBC', 'D': 'edgeAD', 'E': 'edgeEF', 'C': 'edgeCD', 'F': 'edgeFC'}


def test_ap():

    A = Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train")
    B = Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train")
    C = Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train")
    D = Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train")
    E = Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train")
    F = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train")
    G = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 7, "line", "train")
    H = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 8, "line", "train")

    vertices = []
    vertices.append(A)
    vertices.append(B)
    vertices.append(C)
    vertices.append(D)
    vertices.append(E)
    vertices.append(F)
    vertices.append(G)
    vertices.append(H)

    this_graph = Graph(vertices, 8)

    edgeAB = Edges("line", 3, "edgeAB")
    edgeAC = Edges("line", 1, "edgeAC")
    edgeBC = Edges("line", 1, "edgeBC")

    edgeCD = Edges("line", 1, "edgeCD")
    edgeDE = Edges("line", 6, "edgeDE")

    edgeEF = Edges("line", 2, "edgeEF")
    edgeFG = Edges("line", 4, "edgeFG")
    edgeEG = Edges("line", 5, "edgeEG")
    edgeFH = Edges("line", 4, "edgeFH")

    this_graph.add_edge(0, B, edgeAB)
    this_graph.add_edge(0, C, edgeAC)
        
    this_graph.add_edge(1, A, edgeAB)
    this_graph.add_edge(1, C, edgeBC)

    this_graph.add_edge(2, B, edgeBC)
    this_graph.add_edge(2, D, edgeCD)
    this_graph.add_edge(2, A, edgeAC)

    this_graph.add_edge(3, E, edgeDE)
    this_graph.add_edge(3, C, edgeCD)

    this_graph.add_edge(4, G, edgeEG)
    this_graph.add_edge(4, D, edgeDE)
    this_graph.add_edge(4, F, edgeEF)

    this_graph.add_edge(5, H, edgeFH)
    this_graph.add_edge(5, G, edgeFG)
    this_graph.add_edge(5, E, edgeEF)

    this_graph.add_edge(6, F, edgeFG)
    this_graph.add_edge(6, E, edgeEG)

    this_graph.add_edge(7, F, edgeFH)

    assert this_graph.findArticulationPoints(this_graph.graph[0].get_vertex()) == ['E', 'D', 'C']


def test_findCycle():

    A = Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train")
    B = Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train")
    C = Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train")
    D = Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train")
    E = Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train")
    F = Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train")

    vertices = []
    vertices.append(A)
    vertices.append(B)
    vertices.append(C)
    vertices.append(D)
    vertices.append(E)
    vertices.append(F)

    this_graph = Graph(vertices, 6)

    edgeAB = Edges("line", 3, "edgeAB")
    edgeAF = Edges("line", 1, "edgeAF")

    edgeCD = Edges("line", 1, "edgeCD")
    edgeDE = Edges("line", 6, "edgeDE")

    edgeBC = Edges("line", 2, "edgeBC")
    edgeBE = Edges("line", 4, "edgeBE")

    this_graph.add_edge(0, B, edgeAB)
    this_graph.add_edge(0, F, edgeAF)
        
    this_graph.add_edge(1, A, edgeAB)
    this_graph.add_edge(1, E, edgeBE)
    this_graph.add_edge(1, C, edgeBC)

    this_graph.add_edge(2, B, edgeBC)
    this_graph.add_edge(2, D, edgeCD)

    this_graph.add_edge(3, E, edgeDE)
    this_graph.add_edge(3, C, edgeCD)

    this_graph.add_edge(4, B, edgeBE)
    this_graph.add_edge(4, D, edgeDE)

    this_graph.add_edge(5, A, edgeAF)

    assert this_graph.findCycle(6) == True
  



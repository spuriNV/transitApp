import pytest
import main as main
from main import MinHeap
from main import Node 
from main import Vertex
from main import Edges

# pytest minheap_test.py

@pytest.fixture
def my_minheap():
        return MinHeap(6)

def test_parent(my_minheap):
    assert my_minheap.parent(6) == 3

def test_leftChild(my_minheap):
    assert my_minheap.leftChild(3) == 6

def test_rightChild(my_minheap):
    assert my_minheap.rightChild(2) == 5

def test_insert_and_isLeaf(my_minheap):
    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))
    node3 = Node(Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train"))
    node4 = Node(Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train"))
    node5 = Node(Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train"))
    node6 = Node(Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))
    node3.set_edge(Edges("line", 3, "none"))
    node4.set_edge(Edges("line", 4, "none"))
    node5.set_edge(Edges("line", 5, "none"))
    node6.set_edge(Edges("line", 6, "none"))

    my_minheap.insert(node1)
    my_minheap.insert(node2)
    my_minheap.insert(node3)
    my_minheap.insert(node4)
    my_minheap.insert(node5)
    my_minheap.insert(node6)

    assert my_minheap.isLeaf(4) == True 
    assert my_minheap.isLeaf(2) == False


def test_swap(my_minheap):
    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))
    node3 = Node(Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train"))
    node4 = Node(Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train"))
    node5 = Node(Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train"))
    node6 = Node(Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))
    node3.set_edge(Edges("line", 3, "none"))
    node4.set_edge(Edges("line", 4, "none"))
    node5.set_edge(Edges("line", 5, "none"))
    node6.set_edge(Edges("line", 6, "none"))

    my_minheap.insert(node1)
    my_minheap.insert(node2)
    my_minheap.insert(node3)
    my_minheap.insert(node4)
    my_minheap.insert(node5)
    my_minheap.insert(node6)

    my_minheap.swap(6, 3)

    assert my_minheap.Heap[3].get_edge().get_weight() == 6
    assert my_minheap.Heap[6].get_edge().get_weight() == 3


def test_size(my_minheap):

    assert my_minheap.size == 0

    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))
    node3 = Node(Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))
    node3.set_edge(Edges("line", 3, "none"))

    my_minheap.insert(node1)
    my_minheap.insert(node2)
    my_minheap.insert(node3)

    assert my_minheap.size == 3


def test_searchHeap(my_minheap):
    assert my_minheap.searchHeap("example") == -1 

    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))

    my_minheap.insert(node1)
    my_minheap.insert(node2)

    assert my_minheap.searchHeap("A") == 1



def test_remove(my_minheap):
    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))
    node3 = Node(Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))
    node3.set_edge(Edges("line", 3, "none"))

    my_minheap.insert(node1)
    my_minheap.insert(node2)
    my_minheap.insert(node3)

    assert my_minheap.Heap[1].get_edge().get_weight() == 1
    my_minheap.remove()
    assert my_minheap.Heap[1].get_edge().get_weight() == 2



def test_minheap_minheapify(my_minheap):
    node1 = Node(Vertex("d3448824-dbcd-4e71-984c-cd78bd7844ef", "A", 1, "line", "train"))
    node2 = Node(Vertex("0a9e49f1-3ff1-46bd-9bcf-63e850e5791b", "B", 2, "line", "train"))
    node3 = Node(Vertex("4af3d703-ce91-4247-bf92-b141be8bf599", "C", 3, "line", "train"))
    node4 = Node(Vertex("15593864-b026-4514-9e5e-603cdaed1e0d", "D", 4, "line", "train"))
    node5 = Node(Vertex("f52208d0-011f-4f25-8f41-6b7eba294fd4", "E", 5, "line", "train"))
    node6 = Node(Vertex("fb9e82bc-e65f-40ec-8dd7-c174576bd025", "F", 6, "line", "train"))

    node1.set_edge(Edges("line", 1, "none"))
    node2.set_edge(Edges("line", 2, "none"))
    node3.set_edge(Edges("line", 3, "none"))
    node4.set_edge(Edges("line", 4, "none"))
    node5.set_edge(Edges("line", 5, "none"))
    node6.set_edge(Edges("line", 6, "none"))

    my_minheap.insert(node6)
    my_minheap.insert(node5)
    my_minheap.insert(node4)
    my_minheap.insert(node3)
    my_minheap.insert(node2)
    my_minheap.insert(node1)

    assert my_minheap.Heap[1].get_edge().get_weight() == 1
    assert my_minheap.Heap[2].get_edge().get_weight() == 3
    assert my_minheap.Heap[3].get_edge().get_weight() == 2
    assert my_minheap.Heap[4].get_edge().get_weight() == 6
    assert my_minheap.Heap[5].get_edge().get_weight() == 4
    assert my_minheap.Heap[6].get_edge().get_weight() == 5

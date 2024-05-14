import pytest
import main as main
from main import Node
from main import Vertex

# pytest node_test.py

@pytest.fixture
def my_node():
    this_vertex = Vertex("0b288822-41c9-49ba-b88b-0313ccd7f1c0", "A", 1, "line", "train")
    return Node(this_vertex)

def test_vertex(my_node):
    other_vertex = Vertex("0b288822-41c9-49ba-b88b-0313ccd7f1c0", "A", 1, "line", "train")
    assert my_node.get_vertex().get_id() == other_vertex.get_id()
    assert my_node.get_vertex().get_name() == other_vertex.get_name()
    assert my_node.get_vertex().get_line_num() == other_vertex.get_line_num()
    assert my_node.get_vertex().get_mode() == other_vertex.get_mode()

def test_edge(my_node):
    assert my_node.get_edge() == None 
    my_node.set_edge(2)
    assert my_node.get_edge() == 2

def test_next(my_node):
    assert my_node.get_next() == None 

    this_vertex = Vertex("0b288822-41c9-49ba-b88b-0313ccd7f1c0", "B", 2, "line", "train")
    otherNode = Node(this_vertex)

    my_node.set_next(otherNode)
    assert my_node.get_next() == otherNode





    
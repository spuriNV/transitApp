import pytest
import main as main
from main import Vertex

# pytest vertex_test.py

@pytest.fixture
def my_vertex():
        return Vertex("0b288822-41c9-49ba-b88b-0313ccd7f1c0", "A", 1, "line", "train")

def test_name(my_vertex):
        assert my_vertex.get_name() == "A"
        my_vertex.set_name("B")
        assert my_vertex.get_name() == "B"

def test_stopId(my_vertex):
        assert my_vertex.get_stopId() == 1
        my_vertex.set_stopId(2)
        assert my_vertex.get_stopId() == 2

def test_lineNum(my_vertex):
        assert my_vertex.get_line_num() == "line"
        my_vertex.set_line_num("newLine")
        assert my_vertex.get_line_num() == "newLine"

def test_mode(my_vertex):
        assert my_vertex.get_mode() == "train"
        my_vertex.set_mode("bus")
        assert my_vertex.get_mode() == "bus"

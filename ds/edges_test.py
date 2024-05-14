import pytest
import main as main
from main import Edges

# pytest edges_test.py

@pytest.fixture
def my_edges():
        return Edges("lineType", -1, "")

def test_weight(my_edges):
        assert my_edges.get_weight() == -1
        my_edges.set_weight(2)
        assert my_edges.get_weight() == 2

def test_line(my_edges):
        assert my_edges.get_line() == "lineType"
        my_edges.set_line("otherLineType")
        assert my_edges.get_line() == "otherLineType"

def test_name(my_edges):
        assert my_edges.get_name() == ""
        my_edges.set_name("exampleName")
        assert my_edges.get_name() == "exampleName"


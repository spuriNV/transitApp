import pytest
import main as main
from main import DisjointSet

# pytest disjointSet_test.py

@pytest.fixture
def my_disjset():
        return DisjointSet()

def test_makeSet(my_disjset):
    parent = {}
    for i in range(4):
        parent[i] = i

    my_disjset.makeSet(4)
    assert my_disjset.parent == parent

def test_find_union(my_disjset):
        my_disjset.makeSet(3)
        my_disjset.union(1, 0)
        assert my_disjset.find(1) == 0

        my_disjset.union(2, 1)
        assert my_disjset.find(2) == 0
        assert my_disjset.find(1) == 0





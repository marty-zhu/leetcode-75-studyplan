import os
import sys
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from solutions.n724_pivot_index import pivot_index

class TestPivotIndex:

    @pytest.mark.xfail(reason="function not written yet as per TDD.")
    def test_none_edge_index():
        pass

    @pytest.mark.xfail(reason="function not written yet as per TDD.")
    def test_left_edge_index():
        pass

    @pytest.mark.xfail(reason="function not written yet as per TDD.")
    def test_right_edge_index():
        pass

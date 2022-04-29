import pytest

from median_heap import MedianHeap
from test_utils import is_module_in_stl


@pytest.fixture
def gloabal_median_heap():
    return MedianHeap()


class TestHeapValidity:
    def test_positive_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values([1, 2, 3, 4, 5])
        assert gloabal_median_heap.get_median() == 3

    def test_negative_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values([-1, -2, -3, -4, -5])
        assert gloabal_median_heap.get_median() == -3

    def test_even_list_length(self, gloabal_median_heap):
        gloabal_median_heap.add_values([1, 2, 3, 4, 5, 6])
        assert gloabal_median_heap.get_median() == 3.5

    def test_unordered_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values([3, 5, 1, 4, 2])
        assert gloabal_median_heap.get_median() == 3

    def test_large_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values(
            [
                1_000_000_000_000,
                2_000_000_000_000,
                3_000_000_000_000,
                4_000_000_000_000,
                5_000_000_000_000,
            ]
        )
        assert gloabal_median_heap.get_median() == 3_000_000_000_000

    def test_equal_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values([2, 2, 2, 2, 2, 2, 2])
        assert gloabal_median_heap.get_median() == 2

    def test_many_numbers(self, gloabal_median_heap):
        gloabal_median_heap.add_values([x for x in range(10_000_001)])
        assert gloabal_median_heap.get_median() == 5_000_000

    def test_heap_is_balanced(self, gloabal_median_heap):
        gloabal_median_heap.add_values([x for x in range(101)])
        assert (
            abs(len(gloabal_median_heap.min_heap) - len(gloabal_median_heap.max_heap))
            <= 1
        )


def test_using_stl_python_libraries():
    """
    A test just for fun! One of the requirements for the task is to only
    use Python algorithms and structures from Python's standard library.
    So I created a test for that;
    """
    used_python_libraries = ["heapq", "typing"]

    for used_python_library in used_python_libraries:
        assert is_module_in_stl(used_python_library)

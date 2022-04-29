import heapq
from typing import List


class MedianHeap:
    """
    A class used to represent a Median heap data structure
    """

    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []

    def _balance_heap(self) -> None:
        """
        Balances the median heap if the heap becomes unbalanced on either of the max or min heaps

        Complexity: O(logn)
        """
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def add_values(self, values: List[float]) -> None:
        """
        Adds a collection of values one by one to the median heap.
        Note that this was exposed solely for the purpose of testing.

        Complexity: O(nlogn)

        Args:
            values (List[float]): The collection of values to be added to the median heap
        """
        for value in values:
            self.add_value(value)

    def add_value(self, value: float) -> None:
        """
        Adds a single value to the median heap

        Complexity: O(logn)

        Args:
            value (float): The value to be added to the median heap

        Raises:
            TypeError: If the value is not a number (float/int)
        """
        if not isinstance(value, (float, int)):
            raise TypeError("Values should be numbers.")

        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.max_heap, value)
            return

        if value >= self.max_heap[0]:
            heapq.heappush(self.max_heap, value)
        else:
            heapq.heappush(self.min_heap, -value)

        self._balance_heap()

    def get_median(self) -> float:
        """
        Returns the current median of the median heap

        Complexity: O(1)

        Returns:
            float: The current heap median
        """
        length_difference = len(self.max_heap) - len(self.min_heap)

        if length_difference == 0:
            return (-self.min_heap[0] + self.max_heap[0]) / 2

        if length_difference > 0:
            return self.max_heap[0]

        if length_difference < 0:
            return -self.min_heap[0]

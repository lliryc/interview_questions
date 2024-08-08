from typing import List
import heapq
from collections import defaultdict

class Solution:
    """
    A class to solve the Median Sliding Window problem.
    """

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Calculate the median for each sliding window of size k in the given array.

        Args:
            nums (List[int]): The input array of integers.
            k (int): The size of the sliding window.

        Returns:
            List[float]: A list of medians for each sliding window.
        """
        n = len(nums)
        if k == 1 or n == 1:
            return [float(num) for num in nums]

        # Initialize the first window
        knums = sorted(nums[:k])
        hk = k // 2
        maxheap = [-num for num in knums[:hk]]
        minheap = knums[hk:]
        heapq.heapify(maxheap)
        heapq.heapify(minheap)

        # Calculate the first median
        median = float(minheap[0]) if k % 2 else (minheap[0] - maxheap[0]) / 2.0
        medians = [median]

        outnums = defaultdict(int)
        for i in range(1, n - k + 1):
            outnum, innum = nums[i - 1], nums[i + k - 1]
            outnums[outnum] += 1
            
            # Adjust balance
            balance = -1 if outnum <= -maxheap[0] else 1
            balance += -1 if innum <= -maxheap[0] else 1

            # Add new number to appropriate heap
            if innum <= -maxheap[0]:
                heapq.heappush(maxheap, -innum)
            else:
                heapq.heappush(minheap, innum)

            # Rebalance heaps
            self._rebalance_heaps(maxheap, minheap, balance)

            # Remove numbers no longer in the window
            self._remove_outdated(maxheap, outnums, is_maxheap=True)
            self._remove_outdated(minheap, outnums, is_maxheap=False)

            # Calculate new median
            if k % 2 == 0:
                medians.append((minheap[0] - maxheap[0]) / 2.0)
            else:
                medians.append(float(minheap[0]))

        return medians

    def _rebalance_heaps(self, maxheap: List[int], minheap: List[int], balance: int) -> None:
        """
        Rebalance the heaps to maintain the median property.

        Args:
            maxheap (List[int]): The max heap (negated values).
            minheap (List[int]): The min heap.
            balance (int): The balance factor between heaps.
        """
        if balance < 0:
            heapq.heappush(minheap, -heapq.heappop(maxheap))
        elif balance > 0:
            heapq.heappush(maxheap, -heapq.heappop(minheap))

    def _remove_outdated(self, heap: List[int], outnums: defaultdict, is_maxheap: bool) -> None:
        """
        Remove outdated numbers from the heap.

        Args:
            heap (List[int]): The heap to remove numbers from.
            outnums (defaultdict): Dictionary of numbers to be removed.
            is_maxheap (bool): True if the heap is a max heap, False for min heap.
        """
        while heap and (num := (-heap[0] if is_maxheap else heap[0])) in outnums:
            outnums[num] -= 1
            if outnums[num] == 0:
                del outnums[num]
            heapq.heappop(heap)

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_element(self):
        self.assertEqual(self.solution.medianSlidingWindow([1], 1), [1.0])

    def test_window_size_one(self):
        self.assertEqual(self.solution.medianSlidingWindow([1, 2, 3, 4, 5], 1), [1.0, 2.0, 3.0, 4.0, 5.0])

    def test_even_window_size(self):
        self.assertEqual(self.solution.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 2), 
                         [2.0, 1.0, -2.0, 1.0, 4.0, 3.0, 6.5])

    def test_odd_window_size(self):
        self.assertEqual(self.solution.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), 
                         [1.0, -1.0, -1.0, 3.0, 5.0, 6.0])

    def test_repeated_elements(self):
        self.assertEqual(self.solution.medianSlidingWindow([1, 1, 1, 1], 2), [1.0, 1.0, 1.0])

    def test_mixed_elements(self):
        self.assertEqual(self.solution.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3), 
                         [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0])

if __name__ == "__main__":
    unittest.main()


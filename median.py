from typing import List
import heapq
from collections import defaultdict


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        if k == 1 or n == 1:
            return [float(num) for num in nums]
        knums = nums[0:k]
        knums = list(sorted(knums))
        hk = len(knums) // 2
        maxheap = [-k for k in knums[0: hk]]
        heapq.heapify(maxheap)
        minheap = knums[hk:]
        heapq.heapify(minheap)
        if k % 2 == 0:
            median = float(minheap[0] - maxheap[0]) / 2.0
        else:
            median = float(minheap[0])
        medians = [median]
        outnums = defaultdict(int)
        for i in range(1, n-k+1):
            outnum = nums[i-1]
            outnums[outnum] += 1
            balance = 0
            if outnum <= -maxheap[0]:
                balance += 1
            else:
                balance += -1
            knum = nums[i+k-1]
            if knum <= -maxheap[0]:
                heapq.heappush(maxheap, -knum)
                balance+=-1
            else:
                heapq.heappush(minheap, knum)
                balance+=1
            if balance < 0:
                mx = -heapq.heappop(maxheap)
                heapq.heappush(minheap, mx)
            elif balance > 0:
                mx = heapq.heappop(minheap)
                heapq.heappush(maxheap, -mx)
            while -maxheap[0] in outnums:
                outnums[-maxheap[0]] -= 1
                if outnums[-maxheap[0]] == 0:
                    del outnums[-maxheap[0]]
                heapq.heappop(maxheap)
            while minheap[0] in outnums:
                outnums[minheap[0]] -= 1
                if outnums[minheap[0]] == 0:
                    del outnums[minheap[0]]
                heapq.heappop(minheap)


            if k % 2 == 0:
                medians.append(float(minheap[0] - maxheap[0])/2.0)
            else:
                medians.append(float(minheap[0]))
        return medians

s = Solution()
print(s.medianSlidingWindow([1,1,1,1], 2))
print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.medianSlidingWindow([1,2,3,4,2,3,1,4,2], 3))


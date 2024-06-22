from typing import List
from collections import Counter
import math
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freqd = Counter(arr)
        arr = sorted(list(freqd.keys()))
        posd = { c: i for i, c in enumerate(arr) }
        n = len(arr)
        cnt = 0
        # triples
        if target % 3 == 0:
           cnt += math.comb(freqd[target//3], 3)
        # pairs
        for i, item in enumerate(arr):
            key1 = target - 2 * item

            if key1 in posd and posd[key1] > i:
                cnt += math.comb(freqd[item], 2) * freqd[key1]

            if (target - item) % 2 == 0 and not (target % 3 ==0 and target//3 == item):
                key2 = (target - item) // 2
                if key2 in posd and posd[key2] > i:
                    cnt += math.comb(freqd[key2], 2) * freqd[item]
        # uniques
        for i in range(n-2):
            for j in range(i+1, n-1):
                key = target - arr[i] - arr[j]
                if key in posd and posd[key] > j:
                    cnt += freqd[arr[i]] * freqd[arr[j]] * freqd[key]
        return cnt

sol = Solution()

print(sol.threeSumMulti([3,3,3,0], 6))
#print(sol.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
#print(sol.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))






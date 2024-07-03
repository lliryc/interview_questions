from typing import List
from functools import cache
import sys

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def hamming_distance(arr1, arr2):
            return sum(c1 == c2 for c1, c2 in zip(arr1, arr2))

        global buffer
        buffer = list('?' * len(target))
        n = len(target)
        m = len(stamp)
        stamp = list(stamp)
        target = list(target)
        global hops
        hops = 0
        log = []

        def min_stamps(first):
            global hops
            dst = hamming_distance(buffer, target)
            if dst == n:
                hops -= 1
                return True
            if (dst == 0 and not first) or hops >= 10:
                hops -= 1
                return False
            for i in range(n-m + 1):
                old_state = buffer[i:(i + m)]
                if old_state == stamp:
                    continue
                buffer[i: (i + m)] = stamp
                hops += 1
                log.append(i)
                if min_stamps(False):
                    return True
                buffer[i:(i + m)] = old_state
                log.pop()

        min_stamps(True)
        return log

sol = Solution()
print(sol.movesToStamp(stamp = "abc", target = "ababc"))




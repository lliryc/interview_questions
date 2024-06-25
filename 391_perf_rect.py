import bisect
from bisect import bisect_left
from typing import List
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        hlline = []
        hrline = []
        vlline = []
        vrline = []
        for i, r in enumerate(rectangles):
            [x1, y1, x2, y2] = r
            hlpos = bisect.bisect_left(hlline, (x1, i))
            hrpos = bisect.bisect_right(hrline, (x2, i))
            vlpos = bisect.bisect_left(vlline, (y1, i))
            vrpos = bisect.bisect_right(vrline, (y2, i))
            hint = set()
            vint = set()
            pos = hlpos
            while pos >= 0:
                (x10, i0) = hlline[pos]
                if x10 < x1:
                    if y1


        return True




class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        range = right - left
        if range == 0:
            return left
        shift = 1
        acc = 0
        while True:
            if range < 2**shift:

            shift+=1

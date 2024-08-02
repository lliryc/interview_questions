# The knows API is already defined for you.
# return a bool, whether a knows b
import random
def knows(a: int, b: int) -> bool:
    if b == 9:
        return True
    if a == 9:
        return False

    return False#random.choice([True, False])

class Solution:
    def findCelebrity(self, n: int) -> int:
        inpows = [0] * n
        outpows = [0]* n
        hasUnknown = [False] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if hasUnknown[j] == False and outpows[j] == 0:
                    if knows(i,j):
                        inpows[j] +=1
                        outpows[i] +=1
                        if inpows[j] == n - 1:
                            return j
                    else:
                        hasUnknown[j] = True
                if hasUnknown[i] == False and outpows[i] == 0:
                    if knows(j, i):
                        inpows[i] += 1
                        outpows[j] += 1
                        if inpows[i] == n - 1:
                            return i
                    else:
                        hasUnknown[i] = True
        return -1

s = Solution()
print(s.findCelebrity(2))






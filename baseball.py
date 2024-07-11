from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = []
        for c in ops:
            if c == 'C':
                st.pop()
            elif c == 'D':
                st.append(st[-1]*2)
            elif c == '+':
                st.append(st[-1]+st[-2])
            else:
                st.append(int(c))
        return sum(st)

sol = Solution()
print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))


from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        stack = []
        for ast in asteroids:
            if ast < 0:
                while len(stack) > 0 and stack[-1] < -ast:
                    stack.pop()
                if len(stack) == 0:
                    output.append(ast)
                elif stack[-1] == -ast:
                    stack.pop()
            else:
                stack.append(ast)
        output += stack
        return output

s = Solution()
#print(s.asteroidCollision([-2,-1,1,2]))
#print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([10,2,-5]))




from collections import defaultdict
class Solution(object):
    def canCross(self, stones):
        stoness = set(stones)
        mem = defaultdict(set)
        mem[1] = [1]
        last_stone = stones[-1]
        for stone in stones[1:]:
            if last_stone in mem:
                return True
            if stone not in mem:
                continue
            ks = mem[stone]
            del mem[stone]
            for k in ks:
                if (stone + k - 1) in stoness:
                    mem[stone + k - 1].add(k - 1)
                if stone + k in stoness:
                    mem[stone + k].add(k)
                if (stone + k + 1) in stoness:
                    mem[stone + k + 1].add(k + 1)
        return False


s = Solution()

# test 1
print(f'Test 1 = ' + str(s.canCross(stones = [0,1,3,5,6,8,12,17]) == True))

# test 2
print(f'Test 2 = ' + str(s.canCross(stones = [0,1,2,3,4,8,9,11]) == False))

#test 3
print(f'Test 3 = ' + str(s.canCross(stones = [0,1,3,6,10,15,16,21]) == True))


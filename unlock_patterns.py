from typing import List
from collections import defaultdict
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.skip = defaultdict(int)
        self.skip[(1, 3)] = self.skip[(3, 1)] = 1
        self.skip[(1, 7)] = self.skip[(7, 1)] = 1
        self.skip[(7, 9)] = self.skip[(9, 7)] = 1
        self.skip[(3, 9)] = self.skip[(9, 3)] = 1
        self.skip[(2, 8)] = self.skip[(8, 2)] = self.skip[(4, 6)] = self.skip[(6, 4)] = 1
        self.skip[(3, 7)] = self.skip[(7, 3)] = self.skip[(1, 9)] = self.skip[(9, 1)] = 1

    def numberOfPatterns(self, m: int, n: int) -> int:
        digits = set(range(1,10))
        self.n = n
        self.m = m
        res = 0
        res += self.dfs(1, digits, 1) * 4
        res += self.dfs(2, digits, 1) * 4
        res += self.dfs(5, digits, 1)
        return res

    def dfs(self, c, digits, rest):
        if rest == self.n:
            return 1
        digits.remove(c)
        res = 0
        ds = list(digits)
        for d in ds:
            if self.skip[(c,d)] == 1:
                continue
            res += self.dfs(d, digits, rest + 1)
        digits.add(c)
        return res + int(rest >= self.m)

if __name__ == "__main__":
    s = Solution()
    #print(s.numberOfPatterns(1, 1) == 9)
    #print(s.numberOfPatterns(1, 2) == 65)
    print(s.numberOfPatterns(1, 3))

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start_node = head
        end_node = head
        d = 0
        while d < n:
            end_node = end_node.next
            d += 1
        # remove first element
        if end_node is None:
            return start_node.next
        while end_node.next is not None:
            end_node = end_node.next
            start_node = start_node.next
        start_node.next = start_node.next.next
        return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mn = ml = None
        while True:
            pair = list(sorted(filter(lambda l: l is not None,[l1, l2]), key = lambda k: k.val))
            if len(pair) == 0:
                break
            if pair[0] == l1:
                l1 = l1.next
            if pair[0] == l2:
                l2 = l2.next
            if ml is None:
                ml = mn = ListNode(pair[0].val)
            else:
                mn.next = ListNode(pair[0].val)
                mn = mn.next
        return ml


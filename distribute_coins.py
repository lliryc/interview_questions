from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.moves = 0
        self.up(root)
        return self.moves

    def up(self, node):
        if not node:
            return 0
        val_coins = node.val
        left_coins = self.up(node.left)
        if left_coins > 0:
            val_coins += left_coins
        right_coins = self.up(node.right)
        if right_coins > 0:
            val_coins +=right_coins
        if right_coins < 0:
            if val_coins > 0:
                self.coins = min(val_coins, -right_coins)
                self.down(node.right)
            val_coins += right_coins
        if left_coins < 0:
            if val_coins > 0:
                self.coins = min(val_coins, -left_coins)
                self.down(node.left)
            val_coins += left_coins
        if val_coins>0:
            node.val = 1
            val_coins -=1
        else:
            node.val = 0
            val_coins -= 1
        if val_coins > 0:
            self.moves += val_coins
        return val_coins

    def down(self, node):
        if not node:
            return
        if self.coins == 0:
            return
        if node.val == 1:
            return
        self.moves += self.coins
        if node.val == 0:
            node.val = 1
            self.coins -= 1
        self.down(node.left)
        self.down(node.right)


node6 = TreeNode(2)
node5 = TreeNode(0)
node4 = TreeNode(0, right=node6)
node3 = TreeNode(0, right=node5)
node2 = TreeNode(0, left=node3, right=node4)
node1 = TreeNode(4, right=node2)


s = Solution()
# [4,0,null,null,0,null,0]
print(s.distributeCoins(node1))



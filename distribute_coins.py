from typing import Optional
import unittest

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution class for distributing coins in a binary tree."""

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Distribute coins in the binary tree and return the number of moves required.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The number of moves required to distribute the coins.
        """
        if not root:
            return 0
        self.moves = 0
        self._dfs(root)
        return self.moves

    def _dfs(self, node: Optional[TreeNode]) -> int:
        """
        Perform depth-first search to distribute coins.

        Args:
            node (Optional[TreeNode]): The current node being processed.

        Returns:
            int: The number of excess or deficit coins in the subtree.
        """
        if not node:
            return 0

        left_balance = self._dfs(node.left)
        right_balance = self._dfs(node.right)

        self.moves += abs(left_balance) + abs(right_balance)

        return node.val + left_balance + right_balance - 1

class TestSolution(unittest.TestCase):
    """Test cases for the Solution class."""

    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.distributeCoins(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.distributeCoins(root), 0)

    def test_simple_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(self.solution.distributeCoins(root), 2)

    def test_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.distributeCoins(root), 4)

if __name__ == "__main__":
    unittest.main()

# Example usage
def main():
    # Create the tree: [4,0,null,null,0,null,0]
    node6 = TreeNode(2)
    node5 = TreeNode(0)
    node4 = TreeNode(0, right=node6)
    node3 = TreeNode(0, right=node5)
    node2 = TreeNode(0, left=node3, right=node4)
    root = TreeNode(4, right=node2)

    solution = Solution()
    result = solution.distributeCoins(root)
    print(f"Number of moves required: {result}")


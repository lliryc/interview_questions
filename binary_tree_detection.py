class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

MAX = 100000
MIN = -1

def check_step(node, l_bound, r_bound, visited):
    """
    Recursive function to validate the BST properties.

    Args:
    node (Node): The current node in the BST.
    l_bound (int): The lower bound for the current node's data.
    r_bound (int): The upper bound for the current node's data.
    visited (dict): A dictionary to keep track of visited nodes.

    Returns:
    bool: True if the subtree rooted at `node` is a BST, False otherwise.
    """
    if not node:
        return True

    data = node.data

    if data in visited:
        return False
    visited[data] = True

    if not (l_bound < data < r_bound):
        return False

    return (check_step(node.left, l_bound, data, visited) and
            check_step(node.right, data, r_bound, visited))

def check_bst(root):
    """
    Checks if a binary tree is a binary search tree (BST).

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    bool: True if the binary tree is a BST, False otherwise.
    """
    if not root:
        return True

    visited = {root.data: True}
    return (check_step(root.left, MIN, root.data, visited) and
            check_step(root.right, root.data, MAX, visited))

# Unit tests
def test_check_bst():
    # Test case 1: A valid BST
    root1 = Node(5)
    root1.left = Node(2)
    root1.left.left = Node(1)
    root1.right = Node(7)
    root1.right.right = Node(8)
    assert check_bst(root1) == True, "Test case 1 failed"

    # Test case 2: Not a BST (left child greater than root)
    root2 = Node(5)
    root2.left = Node(6)
    root2.right = Node(7)
    assert check_bst(root2) == False, "Test case 2 failed"

    # Test case 3: Not a BST (right child less than root)
    root3 = Node(5)
    root3.left = Node(2)
    root3.right = Node(4)
    assert check_bst(root3) == False, "Test case 3 failed"

    # Test case 4: Empty tree (should be considered a BST)
    assert check_bst(None) == True, "Test case 4 failed"

    # Test case 5: Single node tree (should be considered a BST)
    root5 = Node(10)
    assert check_bst(root5) == True, "Test case 5 failed"

    print("All test cases passed!")

# Running the unit tests
test_check_bst()

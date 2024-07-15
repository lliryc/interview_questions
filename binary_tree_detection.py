# Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

MAX = 100000
MIN = -1

def checkStep(node, lBound, rBound, visited):
    left, right, data = node.left, node.right, node.data

    if data in visited:
        return False
    visited[data] = []

    if lBound > data or data > rBound:
        return False

    if node.left is not None:
        if not checkStep(node.left, lBound, data, visited):
            return False
    if node.right is not None:
        if not checkStep(node.right, data, rBound, visited):
            return False
    return True

def checkBST(root):
    left, right, data = root.left, root.right, root.data
    visited = {data: []}
    if left is not None:
        if not checkStep(left, MIN, data, visited):
            return False
    if right is not None:
        if not checkStep(right, data, MAX, visited):
            return False
    return True

test_root = node(5)
test_root.left = node(2)
test_root.left.left = node(1)
test_root.right = node(7)
test_root.right.right = node(8)

print(checkBST(test_root))

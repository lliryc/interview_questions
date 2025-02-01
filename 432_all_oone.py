class Node:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()   # All keys that have this count.
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        # Create dummy head and tail nodes.
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.key_to_node = {}   # Maps key to the node it resides in.
        self.count_to_node = {} # Maps count value to its node in the list.

    def _insert_node(self, new_node: Node, prev_node: Node, next_node: Node) -> None:
        """Insert new_node between prev_node and next_node."""
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node: Node) -> None:
        """Remove node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # Key is new; its count becomes 1.
            count = 1
            if count in self.count_to_node:
                node = self.count_to_node[count]
            else:
                node = Node(count)
                self.count_to_node[count] = node
                # Insert the new node right after head.
                self._insert_node(node, self.head, self.head.next)
            node.keys.add(key)
            self.key_to_node[key] = node
        else:
            # Key exists; increase its count.
            cur_node = self.key_to_node[key]
            cur_count = cur_node.count
            new_count = cur_count + 1
            # Remove the key from its current node.
            cur_node.keys.remove(key)
            # Check if the node for new_count exists.
            if new_count in self.count_to_node:
                next_node = self.count_to_node[new_count]
            else:
                next_node = Node(new_count)
                self.count_to_node[new_count] = next_node
                # Insert new node right after the current node.
                self._insert_node(next_node, cur_node, cur_node.next)
            next_node.keys.add(key)
            self.key_to_node[key] = next_node
            
            # If the current node becomes empty, remove it.
            if not cur_node.keys:
                self._remove_node(cur_node)
                del self.count_to_node[cur_count]

    def dec(self, key: str) -> None:
        # It is guaranteed that key exists.
        cur_node = self.key_to_node[key]
        cur_count = cur_node.count
        new_count = cur_count - 1
        # Remove the key from its current bucket.
        cur_node.keys.remove(key)
        if new_count == 0:
            # The key should be removed entirely.
            del self.key_to_node[key]
        else:
            # Move the key to the bucket with count new_count.
            if new_count in self.count_to_node:
                prev_node = self.count_to_node[new_count]
            else:
                prev_node = Node(new_count)
                self.count_to_node[new_count] = prev_node
                # Insert new node before the current node.
                self._insert_node(prev_node, cur_node.prev, cur_node)
            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node
        
        # If the current node becomes empty, remove it.
        if not cur_node.keys:
            self._remove_node(cur_node)
            del self.count_to_node[cur_count]

    def getMaxKey(self) -> str:
        # The maximum key is any key in the bucket before the tail dummy.
        if self.tail.prev == self.head:
            return ""
        # Return any key from the bucket.
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # The minimum key is any key in the bucket after the head dummy.
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))


# Example usage:
if __name__ == "__main__":
    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    print(allOne.getMaxKey())  # Expected output: "hello"
    print(allOne.getMinKey())  # Expected output: "hello"
    allOne.inc("leet")
    print(allOne.getMaxKey())  # Expected output: "hello"
    print(allOne.getMinKey())  # Expected output: "leet"

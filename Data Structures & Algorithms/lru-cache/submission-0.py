class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # dummy nodes: left = least recently used side, right = most recently used side
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        # insert right before the dummy right node (most recently used)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.cap:
            # evict the least recently used node (right after left dummy)
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]
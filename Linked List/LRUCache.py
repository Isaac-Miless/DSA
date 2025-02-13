class LRUCache:

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.keyToAddr = {}
        self.capacity = capacity
        
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        addr = self.keyToAddr.get(key, -1)
        if addr == -1:
            return -1
        
        pass
        

    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev = self.next = None

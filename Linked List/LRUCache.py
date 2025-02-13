class LRUCache:
    
    # Suboptimal -- will explore properly later!

    def __init__(self, capacity: int):
        """
        :type capacity: int
        """
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1
        
    def put(self, key: int, value: int) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return
                
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
            
        self.cache.append([key,value])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev = self.next = None

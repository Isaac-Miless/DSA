import random as rand

class RandomizedSet(object):

    def __init__(self):
        # O(1) time
        self.data = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # O(1) time
        if val in self.data: return False
        self.data.append(val)
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # O(n) time :(
        if val not in self.data: return False
        self.data.remove(val)
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        # O(1) time
        if not self.data: return -1

        return rand.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

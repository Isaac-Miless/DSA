class NumberContainers(object):

    def __init__(self):
        self.mp = {} # number -> min heap of indices
        self.map = {} # idx -> number
        

    def change(self, index:int, number:int) -> None:
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        self.map[index] = number
        if number not in self.mp:
            self.mp[number] = []
        heapq.heappush(self.mp[number], index) # push index to min heap of indices
        

    def find(self, number:int) -> int:
        """
        :type number: int
        :rtype: int
        """
        if number not in self.mp: return -1
        while self.mp[number]:
            idx = self.mp[number][0]
            if self.map[idx] == number:
                return idx
            heapq.heappop(self.mp[number]) # pop the index from min heap
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

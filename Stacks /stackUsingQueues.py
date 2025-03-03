from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.pop()

    def top(self):
        """
        :rtype: int
        """
        temp = self.q1.pop()
        self.q1.append(temp)
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

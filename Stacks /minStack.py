class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = 9999999999999
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.smallest: self.smallest = val

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest

    def print(self): print(self.stack)

minStack = MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
print(minStack.getMin()); # return 0
minStack.pop();
print(minStack.top());    # return 2
print(minStack.getMin()); # return 1

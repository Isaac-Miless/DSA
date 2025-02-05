"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return None
        if head in self.map: return self.map[head]
        
        copiedList = Node(head.val)
        self.map[head] = copiedList
        copiedList.next = self.copyRandomList(head.next)
        copiedList.random = self.map.get(head.random)
        
        return copiedList

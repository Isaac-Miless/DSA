"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # if root is None: return
        
        res = []
        # toTraverse = [root]
        self.traverse(root,res)
        
        return res
        
    def traverse(self,root,res):
        if root is None: return
        res.append(root.val)
        
        if root.children:
            for child in root.children:
                self.traverse(child, res)

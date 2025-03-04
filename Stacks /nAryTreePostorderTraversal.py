"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None: return []
        res = []
        # toTraverse = [root]
        
        # while toTraverse:
        #     temp 
        self.traverse(root,res)
            
        return res

    def traverse(self,root,res):
        if root is None: return
        
        for child in root.children:
            self.traverse(child,res)
        res.append(root.val)

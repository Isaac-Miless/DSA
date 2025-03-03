# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        self.preOrder(root, res)
        return res
    
    def preOrder(self, root, res):
        if root is None: return
        res.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.vals = set()
        
        def recover(root, val):
            if root is None: return
            root.val = val
            self.vals.add(val)
            recover(root.left, 2 * val + 1)
            recover(root.right, 2 * val + 2)
        
        recover(root, 0)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.vals

    # def recover(self, root):
    #     if root is None: return
    #     if root.left is not None:
    #         root.left.val = 2 * root.val + 1
    #         self.recover(root.left)
    #     if root.right is not None:
    #         root.right.val = 2 * root.val + 2
    #         self.recover(root.right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

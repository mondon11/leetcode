#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(1)

class Tree(object):
    def __init__(self,x=None):
        self.root = x

    def add(self,item):
        node = TreeNode(item)
        if not self.root:
            self.root = node
            return

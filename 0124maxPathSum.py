# coding = utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.max_score = float('-inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node):
            if node == None:
                return 0
            left = max(max_gain(node.left),0)
            right = max(max_gain(node.right),0)
            cur_score = node.val + max(left,right)
            new_score = node.val + left + right
            self.max_score = max(new_score,self.max_score)
            return cur_score
        max_gain(root)
        return self.max_score
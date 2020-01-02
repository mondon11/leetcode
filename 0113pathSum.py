# coding = utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _sum(self,li):
        return sum(li)
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        rt = []
        li = []
        def helper(node, li):
            if not node:
                return
            if node.left == None and node.right == None:
                li.append(node.val)
                rt.append(li)
                return
            helper(node.left,li+[node.val])
            helper(node.right,li+[node.val])
        helper(root,li)
        print(rt)
        res = []
        for item in rt:
            if self._sum(item) == sum:
                res.append(item)
        return res

    def pathSum1(self, root, sum):
        rt = []
        li = []

        def helper(node, li, target):
            if not node:
                return
            if node.left == None and node.right == None and target - node.val == 0:
                li.append(node.val)
                rt.append(li)
                return
            helper(node.left, li + [node.val], target - node.val)
            helper(node.right, li + [node.val], target - node.val)

        helper(root, li, sum)
        return rt

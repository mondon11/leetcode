# coding = utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        li = []

        def helper(node, res):
            if not node:
                return

            res = res + node.val

            if node.left == None and node.right == None:
                li.append(res)
                # print(li)
                # if res == sum:
                # return True
                # return False

            helper(node.left, res)
            helper(node.right, res)

        helper(root, 0)
        print(li)
        for item in li:
            if item == sum:
                return True
        return False

    def hasPathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum = sum - root.val
        if root.left == None and root.right == None:
            return sum == 0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root,res):
            if not root:
                return
            helper(root.left,res)
            helper(root.right,res)
            res.append(root.val)
        res = []
        helper(root,res)
        return res

    def postorderTraversal1(self,root):
        Y = 1
        N = 0
        stack = [(N,root)]
        res = []
        while stack:
            t,node = stack.pop()
            if not node:
                continue
            if t == N:
                stack.append((Y, node))
                stack.append((N,node.right))
                stack.append((N,node.left))
            if t == Y:
                res.append(node.val)
        return res
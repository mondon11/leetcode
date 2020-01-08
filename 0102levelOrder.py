# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            stack_ = []
            tmp = []
            while stack:
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack_.append(node.left)
                if node.right:
                    stack_.append(node.right)
            stack = stack_
            res.append(tmp)
        return res

    def levelOrder1(self,root):
        def helper(root,level,res):
            if not root:
                return
            if level == len(res):
                res.append([])
            res[level].append(root.val)
            helper(root.left,level+1,res)
            helper(root.right,level+1,res)
        res = []
        helper(root,0,res)
        return res

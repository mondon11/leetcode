# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = [root]
        while stack:
            _stack = []
            level = []
            while stack:
                node = stack.pop(0)
                if not node:
                    level.append('null')
                    continue
                _stack.append(node.left)
                _stack.append(node.right)
                level.append(node.val)
            stack = _stack
            print(level)
            if not self.isListSymmetric(level):
                return False
        return True

    def isListSymmetric(self,li):
        if not li:
            return True
        lth = len(li)
        head = 0
        tail = lth-1
        while(head<tail):
            if li[head] != li[tail]:
                return False
            head = head + 1
            tail = tail - 1
        return True

    def isSymmetric1(self, root):
        if not root:
            return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):
        if left == None and right == None:
            return True
        if left == None and right != None:
            return False
        if left != None and right == None:
            return False
        return(left.val == right.val and self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left))

    def isSymmetric2(self, root):
        if not root:
            return True
        stack = [root.right,root.left]
        while stack:
            left = stack.pop()
            right = stack.pop()
            if left == None and right != None:
                return False
            if left != None and right == None:
                return False
            if left == None and right == None:
                continue
            if left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isListSymmetric([1]))
# Definition for a binary tree node.
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

        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1




class Tree(object):
    def __init__(self,node = None):
        self.root = node

    def add(self,item):
        node = TreeNode(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.val == None:
                continue
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.left)
                queue.append(cur_node.right)

    def floor_travel(self):
        if self.root == None:
            return []
        li = []
        my_queue = [self.root]
        while my_queue:
            cur_node = my_queue.pop(0)
            if cur_node:
                li.append(cur_node.val)
                # print(cur_node.val)
                if cur_node.left:
                    my_queue.append(cur_node.left)
                if cur_node.right:
                    my_queue.append(cur_node.right)
        return li

    def front_travl(self):
        if self.root == None:
            return []
        li = []
        def helper(root):
            if not root:
                return
            li.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(self.root)
        return li


if __name__ == '__main__':
    li = [1,2,None,3,None,4,None,5]
    myTree = Tree()
    for i in li:
        myTree.add(i)
    print(myTree.floor_travel())
    print(myTree.front_travl())
    sol = Solution()
    print(sol.maxDepth(myTree.root))





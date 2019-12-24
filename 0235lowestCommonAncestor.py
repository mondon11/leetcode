# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

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

    def front_travel(self):
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

    def mid_travel(self):
        if self.root == None:
            return []
        li = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            li.append(root.val)
            helper(root.right)
        helper(self.root)
        return li

if __name__ == '__main__':
    li = [6,2,8,0,4,7,9,None,None,3,5]
    myTree = Tree()
    for i in li:
        myTree.add(i)
    print(myTree.floor_travel())
    print(myTree.front_travel())
    print(myTree.mid_travel())
    sol = Solution()
    sol.lowestCommonAncestor(myTree.root,)
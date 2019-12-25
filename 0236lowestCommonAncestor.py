# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = None

    def lowestCommonAncestor1(self, root,p,q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        dic = {}
        my_queue = [root]
        while my_queue:
            cur_node = my_queue.pop(0)
            if cur_node:
                if cur_node.left and cur_node.left.val is not None:
                    dic[cur_node.left.val]=cur_node.val
                    my_queue.append(cur_node.left)
                if cur_node.right and cur_node.right.val is not None:
                    dic[cur_node.right.val]=cur_node.val
                    my_queue.append(cur_node.right)

        print(dic)

        res = {root.val:[root.val]}
        def generateAncestors(dic,key,k):
            if key not in dic.keys():
                return
            else:
                if not res.get(k):
                    res[k] = [k]
                res[k].append(dic[key])
                print(res)
                return generateAncestors(dic,dic[key],k)


        for k in dic.keys():
            generateAncestors(dic,k,k)
        print(res)
        p_anc = res.get(p.val)
        q_anc = res.get(q.val)
        for i in p_anc:
            if i in q_anc:
                my_queue = [root]
                while my_queue:
                    cur_node = my_queue.pop(0)
                    if cur_node:
                        if cur_node.val == i:
                            print(cur_node)
                            return cur_node
                        # print(cur_node.val)
                        if cur_node.left:
                            my_queue.append(cur_node.left)
                        if cur_node.right:
                            my_queue.append(cur_node.right)

    def lowestCommonAncestor2(self, root,p,q):
        dic = {}
        my_queue = [root]
        while my_queue:
            cur_node = my_queue.pop(0)
            if cur_node:
                if cur_node.left and cur_node.left.val is not None:
                    dic[cur_node.left]=cur_node
                    my_queue.append(cur_node.left)
                if cur_node.right and cur_node.right.val is not None:
                    dic[cur_node.right]=cur_node
                    my_queue.append(cur_node.right)

        #print(dic)
        l = p
        r = q
        while(l!=r):
            l = dic.get(l,q)
            r = dic.get(r,p)
        return l

    def lowestCommonAncestor(self, root,p,q):
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                self.res = root
                return True

            if (root.val == p.val or root.val == q.val) and (left or right):
                self.res = root
                return True

            if left or right:
                return True

            if (root.val == p.val or root.val == q.val):
                return True

            return False
        dfs(root)
        return self.res


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

if __name__ == '__main__':
    li = [3,5,1,6,2,0,8,None,None,7,4]
    myTree = Tree()
    for i in li:
        myTree.add(i)
    print(myTree.floor_travel())
    sol = Solution()
    sol.lowestCommonAncestor(myTree.root,myTree.root,myTree.root)
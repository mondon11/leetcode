# class LRUCache(object):
#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.capacity = capacity
#         self.dic = {}
#         self.li = []
#
#
#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         r = self.dic.get(key)
#
#         if r is None:
#             return -1
#         else:
#             self.li.remove(key)
#             self.li.append(key)
#             return r
#
#
#
#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if len(self.dic)>= self.capacity and key not in self.dic.keys():
#             tmp = self.li[0]
#             self.dic.pop(tmp)
#             self.li.remove(tmp)
#         self.dic[key]=value
#         self.li.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DListNode(object):
    def __init__(self,key = None,value = None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def move_node_to_tail(self,key):
        node = self.dic[key]
        node.pre.next = node.next
        node.next.pre = node.pre

        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.dic.get(key)
        if node is None:
            return -1
        else:
            self.move_node_to_tail(key)
            return node.value




    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic.keys():
            self.dic[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.dic) >= self.capacity:
                self.dic.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            node = DListNode(key,value)
            self.dic[key] = node
            node.pre = self.tail.pre
            node.next = self.tail
            self.tail.pre.next = node
            self.tail.pre = node


if __name__ == '__main__':
    sol = LRUCache(2)
    sol.put(1,1)
    sol.put(2,2)
    sol.get(1)
    sol.put(3,3)
    sol.get(2)
    sol.put(4,4)
    sol.get(1)
    sol.get(3)
    sol.get(4)
    print(1)

# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

from collections import defaultdict

class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleList(object):
    def __init__(self):
        self.head = None
        self.tail = None

        pass
    def move(self, position, list, node):
        position.prev = node
        node.prev.next = None
        node.next = position
        list.head = node
        pass
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyMap = defaultdict(lambda: None)
        self.list = DoubleList()
        self.len = 0
        # self.LRUList = list()
        # self.LRUMap = defaultdict(lambda: None)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keyMap:
            p = self.keyMap[key]
            self.list.move(self.list.head, self.list, p)
            return p.value
        else:
            return -1
        # if self.LRUMap[key] != None:
        #     return self.LRUList[self.LRUMap[key]]
        # else:
        #     return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if self.capacity == len(self.LRUList):
        #     for i in self.LRUMap:
        #         if self.LRUMap[i] == 0:
        #             del self.LRUMap[i]
        #         else:
        #             self.LRUMap[i] = self.LRUMap[i] - 1
        # if self.LRUMap[key]:
        #     index = self.LRUMap[key]
        #     self.LRUList = self.LRUList[:index] + self.LRUList[index + 1:] + [value]
        #     for i in self.LRUMap:
        #         if i > index:
        #             self.LRUMap[i] = self.LRUMap[i] - 1
        #     self.LRUMap[key] = len(self.LRUList)
        # else:
        #     self.LRUList.append(value)
        #     self.LRUMap[key] = len(self.LRUList) - 1

lru = LRUCache(2)

lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))    
lru.put(3, 3)    
print(lru.get(2)) 
# lru.put(4, 4)    
# lru.get(1)     
# lru.get(3)       
# lru.get(4)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


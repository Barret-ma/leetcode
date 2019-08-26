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

    def move(self, position, list, node):
        
        # if node.prev != None:
        #     node.prev.next = node.next
        # if node.next != None:
        #     node.next.prev = node.prev
        if node == position:
            return
        prevP = node.prev
        nextP = node.next
        if self.tail == node and prevP != None:
            self.tail = prevP
        if list.head.next != None:
            node.prev = None
            position.prev = node
            node.next = position
            list.head = node
        if prevP != None:
            prevP.next = nextP
        if nextP != None:
            nextP.prev = prevP


    def delTail(self, node):
        key = self.tail.key
        if self.head.next:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        return key
    
    def add(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

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
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keyMap:
            p = self.keyMap[key]
            p.value = value
            self.list.move(self.list.head, self.list, p)
            return
        if self.len < self.capacity:
            node = ListNode(key, value)
            self.keyMap[key] = node
            self.list.add(node)
            self.len = self.len + 1
        else:
            node = ListNode(key, value)
            self.keyMap[key] = node
            delKey = self.list.delTail(node)
            del self.keyMap[delKey]
        

# lru = LRUCache(1)

# lru.put(2, 1)
# print(lru.get(2))
# lru.put(3, 2)
# print(lru.get(2))
# print(lru.get(3))   
# 
# ==========2============ 
# lru = LRUCache(2)

# lru.put(2, 1)    
# lru.put(2, 2)    
# print(lru.get(2))
# lru.put(1, 1)
# lru.put(4, 1)
# print(lru.get(2))


# ==========3==============
# lru = LRUCache(2)

# lru.put(2, 1)  
# lru.put(1, 1)  
# lru.put(2, 3)
# lru.put(4, 1)
# print(lru.get(1))
# print(lru.get(2))


# ==========4==============
# lru = LRUCache(3)

# lru.put(1, 1)  
# lru.put(2, 2)  
# lru.put(3, 3)
# lru.put(4, 4)
# print(lru.get(4))
# print(lru.get(3))
# print(lru.get(2))
# print(lru.get(1))
# lru.put(5, 5)
# print(lru.get(1))
# print(lru.get(2))
# print(lru.get(3))
# print(lru.get(4))
# print(lru.get(5))


# ==========5==============
lru = LRUCache(10)

lru.put(10, 13)
lru.put(3, 17)  
lru.put(6, 11)
lru.put(10, 5)
lru.put(9, 10)

print(lru.get(13))
lru.put(2, 19)
print(lru.get(2))
print(lru.get(3))

lru.put(5, 25)
print(lru.get(8))
lru.put(9, 22)
lru.put(5, 5)
lru.put(1, 30)
print(lru.get(11))
lru.put(9, 12)
print(lru.get(7))
print(lru.get(4))
print(lru.get(5))
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


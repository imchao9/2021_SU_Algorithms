import collections
class LRUCache(object):
    # 模板答案
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.capacity = capacity
        
    def get(self, key):
        # If key doesn't exist
        if key not in self.dic:
            return -1 
        # Key exist
        v = self.dic.pop(key)
        self.dic[key] = v   # update key as the newest one 
        return v 

    def put(self, key, value): 
        # If key already exist
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
        else:
            self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)   
        # Note: OrderedDict popitem removes the items in FIFO(like a queue) order. It accepts a boolean argument last, if it’s set to True then items are returned in LIFO order.

# 因为python里有一种collections.OrderDict()的dict可以维持时间顺序，所以不需要linked list
# ============下面是普通版本的解法
class LRUCache1:
    """
        Data Strcutre: Hashtable<key: int, value: Node>  + Doubly Linked List
        # Why Hashtable? ==> 主要用来实现一个从key to DLL's Node的映射. 另外，it supports O(1）for lookup, insert, delete
        # Why DLL? ==> Dict没有时间观念，所以要用DLL来维护时间顺序。另外，因为需要中间删除，所以要用双向链表，而不是单向的，或者栈这些数据结构
    """
    def __init__(self, capacity: int):
        # Initialize the capacity and the HashTable that use to store datas
        self.capacity = capacity
        self.map = {}   # map<value: int, node: Node>
        # Initialize 带有保护节点的双向链表
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        
    # 就考虑两种情况：1）不存在；2）存在
    def get(self, key: int) -> int:
        if key not in self.map: # 不存在的情况 ==》题目要求，返回-1
            return -1
        # 存在的情况：直接从map里拿出啦，然后返回其value。因为我们选用了DLL来维护时间顺序，所以还用从把对应的Node移到最前面
        node = self.map[key]
        result = node.value
        self.remove_from_list(node)
        self.insert_to_list_head(node.key, node.value)
        return result
    
    # 一样的，考虑两种情况：1）存在，2）不存在
    def put(self, key: int, value: int) -> None:
        # 存在的情况：啥都不用改，直接update时间顺序就好了
        if key in self.map:
            node = self.map[key]
            self.remove_from_list(node)
            self.insert_to_list_head(key, value)
        else: # 不存在，就加入到map 和双链表里
            self.insert_to_list_head(key, value)
        
        if len(self.map)>self.capacity:
            self.remove_from_list(self.tail.pre)

    # 从DLL里移除一个node，就是直接把他pass掉就好了
    def remove_from_list(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        del self.map[node.key]
        # self.map.pop(node.key)

    def insert_to_list_head(self, key, value):
        node = Node(key, value)
        # node 与 下一个点先建立关系
        node.next = self.head.next
        node.next.pre = node
        # node再与head建立关系
        node.pre = self.head 
        self.head.next = node
        # synchronize the map as well
        self.map[key] = node
        return node

class Node:
    def __init__(self, key=None, value=None, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
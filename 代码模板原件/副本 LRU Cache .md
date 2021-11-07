## C/C++ 代码模板

```c++
//C/C++

class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {
        head.next = &tail;
        tail.pre = &head;
    }
    
    int get(int key) {
        if (h.find(key) == h.end()) return -1;
        Node* item = h[key];
        removeFromList(item);
        insertToList(item);
        return item->value;
    }
    
    void put(int key, int value) {
        if (h.find(key) == h.end()) {
            Node* item = new Node();
            item->key = key, item->value = value;
            insertToList(item);
            h[key] = item;
        } else {
            Node* item = h[key];
            item->value = value;
            removeFromList(item);
            insertToList(item);
        }
        if (h.size() > capacity) {
            Node* node = tail.pre;
            removeFromList(node);
            h.erase(node->key);
            delete node;
        }
    }

private:
    struct Node {
        int key;
        int value;
        Node* pre;
        Node* next;
    };

    void removeFromList(Node* node) {
        node->pre->next = node->next;
        node->next->pre = node->pre;
    }

    void insertToList(Node* node) {
        head.next->pre = node;
        node->next = head.next;
        head.next = node;
        node->pre = &head;
    }

    int capacity;
    unordered_map<int, Node*> h;
    Node head, tail;
};
```

## 
## Java代码模板

```java
// Java

public class LRUCache {

    private class Node {
        public int key;
        public int value;
        public Node pre;
        public Node next;
    };
    
    private HashMap<Integer, Node> map;
    // 保护结点
    private Node head;
    private Node tail;
    private int capacity;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<Integer, Node>();
        // 建立带有保护结点的空双向链表
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.pre = head;
    }
    
    public int get(int key) {
        if (!this.map.containsKey(key)) return -1;
        Node node = map.get(key);
        // 从链表和map中删掉
        this.removeFromList(node);
        // 重新插入到map、链表头部，维护时间顺序
        this.insertToListHead(node.key, node.value);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (this.map.containsKey(key)) {
            Node node = this.map.get(key);
            // 从链表中删掉
            this.removeFromList(node);
            // 重新插入到头部，维护时间顺序
            this.insertToListHead(key, value);
        } else {
            // 在链表中插入新结点，返回新结点引用
            this.insertToListHead(key, value);
        }
        if (this.map.size() > this.capacity) {
            this.removeFromList(tail.pre);
        }
    }

    private void removeFromList(Node node) {
        node.pre.next = node.next;
        node.next.pre = node.pre;
        this.map.remove(node.key);
    }

    private Node insertToListHead(int key, int value) {
        Node node = new Node();
        node.key = key;
        node.value = value;
        // node与head的下一个点之间建立联系
        node.next = head.next;
        head.next.pre = node;
        // node与head之间建立联系
        node.pre = head;
        head.next = node;
        // 建立映射关系
        this.map.put(key, node);
        return node;
    }
}
```

## Python代码模板

```python
# Python 

class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

## JavaScript代码模板

```javascript
// JavaScript
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    
    let value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    } else {
      if (this.cache.size >= this.capacity) {
        // Map 中新 set 的元素会放在后面
        let firstKey = this.cache.keys().next();
        this.cache.delete(firstKey.value);
      }
    }
    this.cache.set(key, value);
  }
}
```

## Golang代码模板

```go
package lru

import (
    "container/list"
    "errors"
)

type LRU struct {
    size      int
    innerList *list.List
    innerMap  map[int]*list.Element
}

type entry struct {
    key   int
    value int
}

func NewLRU(size int) (*LRU, error) {
    if size <= 0 {
        return nil, errors.New("must provide a positive size")
    }
    c := &LRU{
        size:      size,
        innerList: list.New(),
        innerMap:  make(map[int]*list.Element),
    }
    return c, nil
}

func (c *LRU) Get(key int) (int, bool) {
    if e, ok := c.innerMap[key]; ok {
        c.innerList.MoveToFront(e)
        return e.Value.(*entry).value, true
    }
    return -1, false
}

func (c *LRU) Put(key int, value int) (evicted bool) {
    if e, ok := c.innerMap[key]; ok {
        c.innerList.MoveToFront(e)
        e.Value.(*entry).value = value
        return false
    } else {
        e := &entry{key, value}
        ent := c.innerList.PushFront(e)
        c.innerMap[key] = ent

        if c.innerList.Len() > c.size {
            last := c.innerList.Back()
            c.innerList.Remove(last)
            delete(c.innerMap, last.Value.(*entry).key)
            return true
        }
        return false
    }
}

```



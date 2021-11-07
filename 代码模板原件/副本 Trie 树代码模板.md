## Python代码模板

```
# Python 
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = [0, {}]  # [count, child]

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.find(word, True, True)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.find(word, True, False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix, False, False)
    
    def find(self, s, exact_match, insert_if_not_exist):
        curr = self.root
        for ch in s:
            if ch not in curr[1]:
                if not insert_if_not_exist:
                    return False
                curr[1][ch] = [0, {}]
            curr = curr[1][ch]
        if insert_if_not_exist:
            curr[0] += 1
        return curr[0] > 0 if exact_match else True

```
## C/C++代码模板

```c++
//C/C++
class Trie {
public:
    /** Initialize your data structure here. */
    Trie() { 
        root = new Node();
    }

    /** Inserts a word into the trie. */
    void insert(string word) { 
        find(word, true, true); 
    }

    /** Returns if the word is in the trie. */
    bool search(string word) { 
        return find(word, true, false); 
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) { 
        return find(prefix, false, false);
    }

private:
    struct Node {
        int count;
        unordered_map<char, Node*> child;
        Node(): count(0) {}
    };
    Node* root;

    bool find(const string& s, bool exact_match, bool insert_if_not_exist) {
        Node* curr = root;
        for (char c : s) {
            if (curr->child.find(c) == curr->child.end()) {
                if (!insert_if_not_exist) return false;
                curr->child[c] = new Node();
            }
            curr = curr->child[c];
        }
        if (insert_if_not_exist) curr->count++;
        return exact_match ? curr->count > 0 : true;
    }
};
```
## Java代码模板

```java
//Java
import java.util.HashMap;
class Trie {
    /** Initialize your data structure here. */
    public Trie() {
        root = new Node();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        find(word, true, true);
    }    

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        return find(word, true, false);
    }    

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        return find(prefix, false, false);
    }

    class Node {
        public int count;
        public HashMap<Character, Node> child;
        public Node() { count = 0; child = new HashMap<>(); }
    }
    Node root;

    boolean find(String s, boolean exact_match, boolean insert_if_not_exist) {
        Node curr = root;
        for (Character c : s.toCharArray()) {
            if (!curr.child.containsKey(c)) {
                if (!insert_if_not_exist) return false;
                curr.child.put(c, new Node());
            }
            curr = curr.child.get(c);
        }
        if (insert_if_not_exist) curr.count++;
        return exact_match ? curr.count > 0 : true;
    }
}
```

## JavaScript代码模板

```javascript
// JavaScript
/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = [0, {}]  // [count, child]
};

Trie.prototype.find = function(word, insertIfNotExist, exactMatch) {
    let curr = this.root
    for (let ch of word) {
        if (!(ch in curr[1])) {
            if (!insertIfNotExist)
                return false
            curr[1][ch] = [0, {}]
        }
        curr = curr[1][ch]
    }
    if (insertIfNotExist)
        curr[0] += 1
    return exactMatch ? curr[0] > 0 : true
};

/**
 * Inserts a word into the trie. 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    return this.find(word, true, false);
};

/**
 * Returns if the word is in the trie. 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    return this.find(word, false, true);
};

/**
 * Returns if there is any word in the trie that starts with the given prefix. 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    return this.find(prefix, false, false);
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
```

## Golang代码模板

```go
// Golang

type Trie struct {
    root *node
}

/** Initialize your data structure here. */
func Constructor() Trie {
    return Trie{root: &node{child: make(map[uint8]*node)}}
}

/** Inserts a word into the trie. */
func (this *Trie) Insert(word string) {
    this.find(word, true, true)
}

/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    return this.find(word, true, false)
}

/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    return this.find(prefix, false, false)
}

type node struct {
    count int
    child map[uint8]*node
}

func (this *Trie) find(s string, exactMatch, insertIfNotExist bool) bool {
    curr := this.root;
    for i := 0; i < len(s); i++ {
        c := s[i]
        if _, ok := curr.child[c]; !ok {
            if !insertIfNotExist {
                return false
            }
            curr.child[c] = &node{child: make(map[uint8]*node)}
        }
        curr = curr.child[c]
    }
    if insertIfNotExist {
        curr.count++
    }
    return !exactMatch || curr.count > 0
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
```


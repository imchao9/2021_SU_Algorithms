import java.util.HashMap;
class Trie {
    public class Node {
        int count; // 词频
        HashMap<Character, Node> child; // 出边（字符映射）
        // Node[] child;
        Node() {
            count = 0;
            child = new HashMap<Character, Node>();
            // child = new Node[26];
        }
    }
    Node root;

    /** Initialize your data structure here. */
    public Trie() {
        // 空字典树：只有根一个点
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        solve(word, true, false);
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        return solve(word, false, false);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        return solve(prefix, false, true);
    }

    private boolean solve(String word, boolean insertIfNotExist, boolean searchPrefix) {
        Node curr = root;
        for (char ch : word.toCharArray()) {
            // if (curr.child[ch - 'a'] == null)
            if (!curr.child.containsKey(ch)) {
                if (insertIfNotExist) {
                    curr.child.put(ch, new Node());
                } else {
                    return false;
                }
            }
            curr = curr.child.get(ch);
        }
        if (searchPrefix) return true;
        if (insertIfNotExist) curr.count++;
        return curr.count > 0;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
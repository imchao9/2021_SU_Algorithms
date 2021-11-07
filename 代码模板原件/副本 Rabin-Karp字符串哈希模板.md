## C/C++代码模板

```c++
// C/C++
// LeetCode 28 实现strStr
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int n = haystack.size();
        int m = needle.size();
        haystack = " " + haystack;
        needle = " " + needle;

        H.push_back(0);
        for (int i = 1; i <= n; i++)
            H.push_back(H[i - 1] * 131 + haystack[i] - 'a' + 1);
        unsigned int val = 0;
        p131.push_back(1);
        for (int i = 1; i <= m; i++) {
            val = val * 131 + needle[i] - 'a' + 1;
            p131.push_back(p131[i - 1] * 131);
        }
        for (int i = m; i <= n; i++) { // 滑动窗结尾
            if (calcHash(i - m + 1, i) == val &&
                haystack.substr(i - m + 1, m) == needle.substr(1, m))
                return i - m; // 下标变回0开始
        }
        return -1;
    }

    // 模板：O(1)得到子串[l..r]的Hash值
    unsigned int calcHash(int l, int r) {
        return H[r] - H[l - 1] * p131[r - l + 1];
    }

private:
    vector<unsigned int> H;
    vector<unsigned int> p131;
};
```

## 
## Java代码模板

```
// Java
// LeetCode 28 实现strStr
class Solution {
    public int strStr(String s, String t) {
        if (t.length() == 0) return 0;
        int n = s.length();
        int m = t.length();
        s = " " + s;
        t = " " + t;

        int p = (int)1e9 + 7; // 10^9+7 是一个质数
        long tHash = 0;
        for (int i = 1; i <= m; i++)
            tHash = (tHash * 131 + (t.charAt(i) - 'a' + 1)) % p;
        // 模板：预处理前缀Hash
        long[] sHash = new long[n + 1];
        sHash[0] = 0;
        long[] p131 = new long[n + 1]; // 131的次幂
        p131[0] = 1;
        for (int i = 1; i <= n; i++) {
            sHash[i] = (sHash[i - 1] * 131 + s.charAt(i) - 'a' + 1) % p;
            p131[i] = p131[i - 1] * 131 % p;
        }
        // hello
        // ll
        for (int i = m; i <= n; i++) { // 滑动窗结尾
            // s[i-m+1 ~ i] 与 t[1..m] 是否相等
            if (calcHash(sHash, p131, p, i - m + 1, i) == tHash &&
                s.substring(i - m + 1, i + 1).equals(t.substring(1))) {
                return i - m; // 下标变回0开始
            }
        }
        return -1;
    }

    // 模板：O(1)得到子串[l..r]的Hash值
    private long calcHash(long[] H, long[] p131, int p, int l, int r) {
        // hello 的子串ll的hash值
        //  hell
        // -he00
        // =  ll
        return ((H[r] - H[l - 1] * p131[r - l + 1]) % p + p) % p;
    }
}
```


## Python代码模板

```
# Python
# LeetCode 28 实现strStr
class Solution:
    def strStr(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 0
        n, m = len(s), len(t)
        s = " " + s
        t = " " + t

        p = int(1e9 + 7)
        tHash = 0
        for i in range(1, m + 1):
            tHash = (tHash * 13331 + ord(t[i])) % p
        # 模板：预处理前缀Hash
        sHash = [0] * (n + 1)
        p13331 = [1] + [0] * n
        for i in range(1, n + 1):
            sHash[i] = (sHash[i - 1] * 13331 + ord(s[i])) % p
            p13331[i] = p13331[i - 1] * 13331 % p

        # 模板：O(1)得到子串[l..r]的Hash值
        # hello 的子串ll的hash值
        #  hell
        # -he00
        # =  ll
        calcHash = lambda l, r: ((sHash[r] - sHash[l - 1] * p13331[r - l + 1]) % p + p) % p
    
        for i in range(m, n + 1): # 滑动窗结尾
            print(calcHash(i - m + 1, i))
            # s[i-m+1 ~ i] 与 t[1..m] 是否相等
            if calcHash(i - m + 1, i) == tHash and s[i - m + 1 : i + 1] == t[1:]:
                return i - m; # 下标变回0开始
        return -1
```

## JavaScript代码模板

```javascript
// JavaScript
// LeetCode 28 实现strStr
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var strStr = function(s, t) {

    if (t.length == 0) return 0;
    let n = s.length;
    let m = t.length;
    s = " " + s;
    t = " " + t;

    const p =  9999991; // 9999991 是一个质数，JavaScript整数没有long，模数不能开太大
    let tHash = 0;
    for (let i = 1; i <= m; i++)
        tHash = (tHash * 13331 + t.charCodeAt(i)) % p;
    // 模板：预处理前缀Hash
    let sHash = [];
    sHash[0] = 0;
    let p13331 = []; // 13331的次幂
    p13331[0] = 1;
    for (let i = 1; i <= n; i++) {
        sHash[i] = (sHash[i - 1] * 13331 + s.charCodeAt(i)) % p;
        p13331[i] = p13331[i - 1] * 13331 % p;
    }

    // 模板：O(1)得到子串[l..r]的Hash值
    var calcHash = function(l, r) {
        // hello 的子串ll的hash值
        //  hell
        // -he00
        // =  ll
        return ((sHash[r] - sHash[l - 1] * p13331[r - l + 1]) % p + p) % p;
    }
  
    for (let i = m; i <= n; i++) { // 滑动窗结尾
        // s[i-m+1 ~ i] 与 t[1..m] 是否相等
        if (calcHash(i - m + 1, i) == tHash &&
            s.substring(i - m + 1, i + 1) == t.substring(1)) {
            return i - m; // 下标变回0开始
        }
    }
    return -1;
};
```

## Golang代码模板

```go
// Golang
// LeetCode 28 实现strStr
func strStr(s, t string) int {
    if t == "" {
        return 0
    }
    n, m := len(s), len(t)
    s = " " + s
    t = " " + t

    p := int64(1e9 + 7) // 10^9+7 是一个质数
    var tHash int64 = 0
    for i := 1; i <= m; i++ {
        tHash = (tHash * 131 + (int64(t[i]) - 'a' + 1)) % p
    }
            
        // 模板：预处理前缀Hash
    sHash := make([]int64, n + 1)
    sHash[0] = 0
    p131 := make([]int64, n + 1) // 131的次幂
    p131[0] = 1;
    for i := 1; i <= n; i++ {
        sHash[i] = (sHash[i - 1] * 131 + (int64(s[i]) - 'a' + 1)) % p
        p131[i] = p131[i - 1] * 131 % p
    }
    // hello
    // ll
    for i := m; i <= n; i++ { // 滑动窗结尾
        // s[i-m+1 ~ i] 与 t[1..m] 是否相等
        if calcHash(sHash, p131, p, i - m + 1, i) == tHash &&
        s[i - m + 1: i + 1] == t[1: ] {
            return i - m // 下标变回0开始
        }
    }
    return -1
}

// 模板：O(1)得到子串[l..r]的Hash值
func calcHash(H, p131 []int64, p int64, l, r int) int64 {
    // hello 的子串ll的hash值
    //  hell
    // -he00
    // =  ll
    return ((H[r] - H[l - 1] * p131[r - l + 1]) % p + p) % p
}
```


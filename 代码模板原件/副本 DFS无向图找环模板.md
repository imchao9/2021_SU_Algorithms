## C/C++代码模板

```c++
//C/C++
// LeetCode684 冗余连接
// 本题有更高效解法，本解法主要练习DFS找环

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for (vector<int>& e : edges) {
            int u = e[0], v = e[1];
            n = max(n, u);
            n = max(n, v);
        }
        // 模板：出边数组初始化
        edge = vector<vector<int>>(n + 1, vector<int>());
        visit = vector<bool>(n + 1, false);
        hasCycle = false;
        for (vector<int>& e : edges) {
            int u = e[0], v = e[1];
            addEdge(u, v);
            addEdge(v, u);
            dfs(u, 0);
            if (hasCycle) return e;
        }
        return {};
    }

private:
    // 模板：DFS无向图找环
    void dfs(int x, int fa) {
        visit[x] = true;
        for (int y : edge[x]) {
            if (y == fa) continue;
            if (!visit[y]) dfs(y, x);
            else hasCycle = true;
        }
        visit[x] = false;
    }

    // 模板：加边
    void addEdge(int x, int y) {
        edge[x].push_back(y);
    }

    int n;
    vector<vector<int>> edge;
    vector<bool> visit;
    bool hasCycle;
};
```

## Java代码模板

```java
// Java
// LeetCode684 冗余连接
// 本题有更高效解法，本解法主要练习DFS找环

class Solution {
    public int[] findRedundantConnection(int[][] input) {
        // 出现过的最大的点就是n
        n = 0;
        for (int[] edge : input) {
            int u = edge[0];
            int v = edge[1];
            n = Math.max(u, n);
            n = Math.max(v, n);
        }

        // 模板：出边数组初始化
        // 初态：[[], [], ... []]
        edges = new ArrayList<List<Integer>>();
        // [false, false, ...]
        visit = new boolean[n + 1];
        for (int i = 0; i <= n; i++) {
            edges.add(new ArrayList<Integer>());
            visit[i] = false;
        }
        hasCycle = false;

        // 加边
        for (int[] edge : input) {
            int u = edge[0];
            int v = edge[1];
            // 无向图看作双向边的有向图
            addEdge(u, v);
            addEdge(v, u);

            // 每加一条边，看图中是否多了环c
            for (int i = 0; i <= n; i++) visit[i] = false;
            dfs(u, -1);
            if (hasCycle) return edge;
        }
        return null;
    }

    // 模板：无向图深度优先遍历找环
    // visit数组，避免重复访问
    // fa是第一次走到x的点
    private void dfs(int x, int fa) {
        // 第一步：标记已访问
        visit[x] = true;
        // 第二步：遍历所有出边
        for (Integer y : edges.get(x)) {
            if (y == fa) continue; // 返回父亲，不是环
            if (visit[y]) hasCycle = true;
            else dfs(y, x);
        }
    }

    // 模板：加边
    private void addEdge(int x, int y) {
        edges.get(x).add(y);
    }

    // 出边数组
    int n;
    private List<List<Integer>> edges;
    boolean hasCycle;
    private boolean[] visit;
}
```

## Python代码模板

```python
# Python
# LeetCode684 冗余连接
# 本题有更高效解法，本解法主要练习DFS找环

class Solution:
    def findRedundantConnection(self, input: List[List[int]]) -> List[int]:
        # 模板：出边数组初始化
        self.edge = [[] for i in range(1001)]  # max n is 1000
        self.hasCycle = False
        for e in input:
            u, v = e[0], e[1]
            self.addEdge(u, v)
            self.addEdge(v, u)
            self.visit = [False] * 1001
            self.dfs(u, -1)
            if self.hasCycle:
                return e
        return []

    # 模板：DFS无向图找环
    def dfs(self, x, fa):
        self.visit[x] = True
        for y in self.edge[x]:
            if y == fa:
                continue
            if self.visit[y]:
                self.hasCycle = True
            else:
                self.dfs(y, x)

    # 模板：加边
    def addEdge(self, u, v):
        self.edge[u].append(v)
```

## JavaScript代码模板

```javascript
// JavaScript
// LeetCode684 冗余连接
// 本题有更高效解法，本解法主要练习DFS找环
/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function(edges) {
    var n = 0
    for (let e of edges) {
        n = Math.max(n, e[0])
        n = Math.max(n, e[1])
    }
    // 模板：出边数组初始化
    var edge = [];
    for (let i = 0; i <= n; i++) edge[i] = [];
    var visit = [];
    var hasCycle = false;

    // 模板：加边
    var addEdge = function(u, v) {
        edge[u].push(v);
    }

    // 模板：DFS无向图找环
    var dfs = function(x, fa) {
        visit[x] = true;
        for (let y of edge[x]) {
            if (y == fa) continue;
            if (visit[y]) hasCycle = true;
            else dfs(y, x);
        }
    }

    for (let e of edges) {
        let u = e[0];
        let v = e[1];
        addEdge(u, v);
        addEdge(v, u);
        for (let i = 0; i <= n; i++) visit[i] = false;
        dfs(u, -1);
        if (hasCycle) return e;
    }
    return [];
};
```

## Golang代码模板

```go
// Golang
// LeetCode684 冗余连接
// 本题有更高效解法，本解法主要练习DFS找环

func findRedundantConnection(edges [][]int) []int {
    n := 0
    for _, e  := range edges {
        if n < e[0] {
            n = e[0]
        }
        if n < e[1] {
            n = e[1]
        }
    }
    // 模板：出边数组初始化
    edge := make([][]int, n + 1)
    visit := make([]bool, n + 1)
    hasCycle := false

    // 模板：加边
    addEdge := func(u, v int) {
        edge[u] = append(edge[u], v)
    }

    // 模板：DFS无向图找环
    var dfs func(int, int)
    dfs = func(x, fa int) {
        visit[x] = true
        for _, y := range edge[x] {
            if y == fa {
                continue
            }
            if visit[y] {
                hasCycle = true
            } else {
                dfs(y, x)
            }
        }
    }

    for _, e := range edges {
        u, v := e[0], e[1]
        addEdge(u, v)
        addEdge(v, u)
        visit = make([]bool, n + 1)
        dfs(u, -1)
        if (hasCycle) {
            return e
        }
    }
    return nil
};
```


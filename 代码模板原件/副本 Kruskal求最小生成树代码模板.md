## Python代码模板

```python
# Python
# LeetCode 1584
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 构造出边
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])])
        # 按边权排序
        edges.sort(key=lambda e: e[2])
        # Kruskal算法
        self.fa = []
        for i in range(n):
            self.fa.append(i)
        ans = 0
        for e in edges:
            x, y, z = self.find(e[0]), self.find(e[1]), e[2]
            if x != y:
                self.fa[x] = y
                ans += z
        return ans
        
    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
```

## C/C++代码模板

```c++
// C/C++
// LeetCode 1584
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        // 构造出边
        vector<vector<int>> edges;
        for (int i = 0; i < points.size(); i++)
            for (int j = i + 1; j < points.size(); j++)
                edges.push_back({i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])});
        // 按照边权排序
        sort(edges.begin(), edges.end(),
             [](const vector<int>& a, const vector<int>&b) {
                 return a[2] < b[2];
             });
        // Kruskal算法
        for (int i = 0; i < points.size(); i++) fa.push_back(i);
        int ans = 0;
        for (int i = 0; i < edges.size(); i++) {
            int x = edges[i][0];
            int y = edges[i][1];
            int z = edges[i][2];
            if (find(x) != find(y)) {
                ans += z;
                fa[find(x)] = find(y);
            }
        }
        return ans;
    }

private:
    vector<int> fa;
    int find(int x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }
};
```

## Java代码模板

```java
// Java
// LeetCode 1584
class Solution {
    public int minCostConnectPoints(int[][] points) {
        // 构造出边
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < points.length; i++)
            for (int j = i + 1; j < points.length; j++)
                edges.add(new int[]{i, j, Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1])});
        // 按照边权排序
        edges.sort((a, b) -> { return a[2] - b[2]; });
        // Kruskal算法
        fa = new int[points.length];
        for (int i = 0; i < points.length; i++) fa[i] = i;
        int ans = 0;
        for (int i = 0; i < edges.size(); i++) {
            int x = edges.get(i)[0];
            int y = edges.get(i)[1];
            int z = edges.get(i)[2];
            if (find(x) != find(y)) {
                ans += z;
                fa[find(x)] = find(y);
            }
        }
        return ans;
    }

    int[] fa;
    int find(int x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }
}
```
   
## JavaScript代码模板

```javascript
/* JavaScript */
// LeetCode 1584
/**
 * @param {number[][]} points
 * @return {number}
 */
var minCostConnectPoints = function(points) {
    let fa = [];
    for (let i = 0; i < points.length; i++) fa[i] = i;
    var find = function(x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }

    // 构造出边
    let edges = [];
    for (let i = 0; i < points.length; i++)
        for (let j = i + 1; j < points.length; j++)
            edges.push([i, j, Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1])]);
    // 按照边权排序
    edges.sort((a, b) => a[2] - b[2]);
    // Kruskal算法
    let ans = 0;
    for (let e of edges) {
        let [x, y, z] = e;
        if (find(x) != find(y)) {
            ans += z;
            fa[find(x)] = find(y);
        }
    }
    return ans;
};
```

## Golang代码模板

```go
// Go
// LeetCode 1584
type unionFind struct {
    parent, rank []int
}

func newUnionFind(n int) *unionFind {
    parent := make([]int, n)
    rank := make([]int, n)
    for i := range parent {
        parent[i] = i
        rank[i] = 1
    }
    return &unionFind{parent, rank}
}

func (uf *unionFind) find(x int) int {
    if uf.parent[x] != x {
        uf.parent[x] = uf.find(uf.parent[x])
    }
    return uf.parent[x]
}

func (uf *unionFind) union(x, y int) bool {
    fx, fy := uf.find(x), uf.find(y)
    if fx == fy {
        return false
    }
    if uf.rank[fx] < uf.rank[fy] {
        fx, fy = fy, fx
    }
    uf.rank[fx] += uf.rank[fy]
    uf.parent[fy] = fx
    return true
}

func dist(p, q []int) int {
    return abs(p[0]-q[0]) + abs(p[1]-q[1])
}

func minCostConnectPoints(points [][]int) (ans int) {
    n := len(points)
    type edge struct{ v, w, dis int }
    edges := []edge{}
    for i, p := range points {
        for j := i + 1; j < n; j++ {
            edges = append(edges, edge{i, j, dist(p, points[j])})
        }
    }

    sort.Slice(edges, func(i, j int) bool { return edges[i].dis < edges[j].dis })

    uf := newUnionFind(n)
    left := n - 1
    for _, e := range edges {
        if uf.union(e.v, e.w) {
            ans += e.dis
            left--
            if left == 0 {
                break
            }
        }
    }
    return
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```



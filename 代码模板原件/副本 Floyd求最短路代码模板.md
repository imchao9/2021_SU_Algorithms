## Python代码模板

```python
# Python
# LeetCode 1334
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 邻接矩阵初值：i到i长度为0，没有边长度为INF，其余为输入的边
        d = [[1e9] * n for i in range(n)]
        for edge in edges:
            x, y, z = edge[0], edge[1], edge[2]
            d[x][y] = d[y][x] = z
        for i in range(n):
            d[i][i] = 0
        # Floyd算法
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        # 统计答案
        ansCount, ans = n, 0
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and d[i][j] <= distanceThreshold:
                    count += 1
            if count <= ansCount:
                ansCount = count
                ans = i
        return ans
```

## C/C++代码模板

```c++
// C/C++
// LeetCode 1334
class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // 邻接矩阵初值：i到i长度为0，没有边长度为INF，其余为输入的边
        vector<vector<int>> d(n, vector<int>(n, 1e9));
        for (auto& edge : edges) {
            int x = edge[0], y = edge[1], z = edge[2];
            d[x][y] = d[y][x] = z;
        }
        for (int i = 0; i < n; i++) d[i][i] = 0;
        // Floyd算法
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        // 统计答案
        int ansCount = n, ans;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++)
                if (i != j && d[i][j] <= distanceThreshold) count++;
            if (count <= ansCount) {
                ansCount = count;
                ans = i;
            }
        }
        return ans;
    }
};
```

## Java代码模板

```java
// Java
// LeetCode 1334
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        // 邻接矩阵初值：i到i长度为0，没有边长度为INF，其余为输入的边
        int[][] d = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                d[i][j] = (int)1e9;
        for (int[] edge : edges) {
            int x = edge[0], y = edge[1], z = edge[2];
            d[x][y] = d[y][x] = z;
        }
        for (int i = 0; i < n; i++) d[i][i] = 0;
        // Floyd算法
        for (int k = 0; k < n; k++)
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
        // 统计答案
        int ansCount = n, ans = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++)
                if (i != j && d[i][j] <= distanceThreshold) count++;
            if (count <= ansCount) {
                ansCount = count;
                ans = i;
            }
        }
        return ans;
    }
}
```
   
## JavaScript代码模板

```javascript
/* JavaScript */
// LeetCode 1334
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} distanceThreshold
 * @return {number}
 */
var findTheCity = function(n, edges, distanceThreshold) {
    // 邻接矩阵初值：i到i长度为0，没有边长度为INF，其余为输入的边
    let d = [];
    for (let i = 0; i < n; i++) {
        d[i] = [];
        for (let j = 0; j < n; j++) d[i][j] = 1e9;
    }
    for (let edge of edges) {
        let x = edge[0], y = edge[1], z = edge[2];
        d[x][y] = d[y][x] = z;
    }
    for (let i = 0; i < n; i++) d[i][i] = 0;
    // Floyd算法
    for (let k = 0; k < n; k++)
        for (let i = 0; i < n; i++)
            for (let j = 0; j < n; j++)
                d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
    // 统计答案
    let ansCount = n, ans = 0;
    for (let i = 0; i < n; i++) {
        let count = 0;
        for (let j = 0; j < n; j++)
            if (i != j && d[i][j] <= distanceThreshold) count++;
        if (count <= ansCount) {
            ansCount = count;
            ans = i;
        }
    }
    return ans;
}
```

## Golang代码模板

```go
// Go
// LeetCode 1334
func findTheCity(n int, edges [][]int, distanceThreshold int) int {
    // 最短路径的状态数组
    var dp [][]int
    // 先初始化
    for i := 0; i < n; i++ {
        var tmp []int
        for j := 0; j < n; j++ { 
            if i == j {
                tmp = append(tmp, 0)
            } else {
                tmp = append(tmp, -1)
            }
        }
        dp = append(dp, tmp)
    }
    // 填出边长
    for i := 0; i < len(edges); i++ {
        from := edges[i][0]
        to := edges[i][1]
        weight := edges[i][2]
        // 无向图
        dp[from][to] = weight
        dp[to][from] = weight
    }
    // dp状态转移方程
    // k放在第一层是因为后面的k要依赖前面的值
    for k := 0; k < n; k++ {
        // 从i到j
        for i := 0; i < n; i++ {
            for j := 0; j < n; j++ {
                // 相同的节点不考虑
                if i == j || i == k || j == k {
                    continue
                }
                // 不通的路也不考虑
                if dp[i][k] == -1 || dp[k][j] == -1 {
                    continue
                }
                tmp := dp[i][k] + dp[k][j]
                if dp[i][j] == -1 || dp[i][j] > tmp {
                    dp[i][j] = tmp
                    dp[j][i] = tmp
                }
            }
        }
    }
    // 统计小于阈值的路径数
    min := n
    idx := 0
    for i := 0; i < n; i++ {
        cnt := 0
        for j := 0; j < n; j++ {
            if i == j {
                continue
            }
            if dp[i][j] <= distanceThreshold {
                cnt++
            }
        }
        if cnt <= min {
            min = cnt
            idx = i
        }
    }
    return idx
}
```



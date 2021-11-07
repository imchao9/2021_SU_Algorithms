## C/C++代码模板

```c++
//C/C++

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        this->m = grid.size();
        this->n = grid[0].size();
        visit = vector<vector<bool>>(m, vector<bool>(n, false));
        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == '1' && !visit[i][j]) {
                    bfs(grid, i, j);
                    ans++;
                }
        return ans;
    }

private:
    // 从(sx,sy)出发bfs
    void bfs(vector<vector<char>>& grid, int sx, int sy) {
        // 长度为2的list或者pair都可以
        queue<pair<int,int>> q;
        // 第一步：push起点
        q.push(make_pair(sx,sy));
        visit[sx][sy] = true;
        while (!q.empty()) {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            // 扩展所有出边（四个方向）
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 任何时候访问数组前，判断合法性
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == '1' && !visit[nx][ny]) {
                    q.push(make_pair(nx, ny));
                    // BFS：入队时标记visit
                    visit[nx][ny] = true;
                }
            }
        }
    }

    int m;
    int n;
    vector<vector<bool>> visit;
    const int dx[4] = {-1, 0, 0, 1};
    const int dy[4] = {0, -1, 1, 0};
};
```

## Java代码模板

```java
//Java

class Solution {
    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        visit = new boolean[m][n];
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                visit[i][j] = false;

        int ans = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == '1' && !visit[i][j]) {
                    bfs(grid, i, j);
                    ans++;
                }
        return ans;
    }

    // 从(sx,sy)出发bfs
    private void bfs(char[][] grid, int sx, int sy) {
        int[] dx = {-1, 0, 0, 1};
        int[] dy = {0, -1, 1, 0};
        Queue<Pair<Integer,Integer>> q = new LinkedList<Pair<Integer,Integer>>();
        // 第一步：push起点
        q.offer(new Pair<Integer,Integer>(sx,sy));
        visit[sx][sy] = true;
        while (!q.isEmpty()) {
            int x = q.peek().getKey();
            int y = q.poll().getValue();
            // 扩展所有出边（四个方向）
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                // 任何时候访问数组前，判断合法性
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == '1' && !visit[nx][ny]) {
                    q.offer(new Pair<Integer,Integer>(nx, ny));
                    // BFS：入队时标记visit
                    visit[nx][ny] = true;
                }
            }
        }
    }

    private int m;
    private int n;
    private boolean[][] visit;
};
```

## Python代码模板

```python
# Python

from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.visit = [[False] * self.n for i in range(self.m)]
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and not self.visit[i][j]:
                    self.bfs(grid, i, j)
                    ans += 1
        return ans

    def bfs(self, grid, sx, sy):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        q = deque()
        # 第一步：push起点
        q.append([sx, sy])
        self.visit[sx][sy] = True
        while len(q) > 0:
            now = q.popleft()
            x, y = now[0], now[1]
            # 扩展所有出边（四个方向）
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 任何时候访问数组前，判断合法性
                if nx < 0 or ny < 0 or nx >= self.m or ny >= self.n:
                    continue
                if grid[nx][ny] == '1' and not self.visit[nx][ny]:
                    q.append([nx, ny])
                    # BFS：入队时标记visit
                    self.visit[nx][ny] = True
```

## JavaScript代码模板

```javascript
//JavaScript

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    var visit = [];
    for (let i = 0; i < m; i++) {
        visit.push([]);
        for (let j = 0; j < n; j++)
            visit[i][j] = false;
    }
    const dx = [-1, 0, 0, 1];
    const dy = [0, -1, 1, 0];

    var bfs = function(sx, sy) {
        var q = []
        // 第一步：push起点
        q.push([sx, sy]);
        visit[sx][sy] = true;
        while (q.length > 0) {
            var now = q.shift();
            var x = now[0];
            var y = now[1];
            // 扩展所有出边（四个方向）
            for (let i = 0; i < 4; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];
                // 任何时候访问数组前，判断合法性
                if (nx < 0 || ny < 0 || nx >= m || ny >= n) continue;
                if (grid[nx][ny] == '1' && !visit[nx][ny]) {
                    q.push([nx, ny]);
                    // BFS：入队时标记visit
                    visit[nx][ny] = true;
                }
            }
        }
    };

    var ans = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] == '1' && !visit[i][j]) {
                bfs(i, j);
                ans++;
            }
    return ans;
};
```

## Golang代码模板

```go
//Golang

func numIslands(grid [][]byte) int {
    m := len(grid)
    n := len(grid[0])
    visit := make([][]bool, 0)
    for i := 0; i < m; i++ {
        visit = append(visit, make([]bool, n))
    }
    dx := []int{-1, 0, 0, 1}
    dy := []int{0, -1, 1, 0}
    var bfs func(int, int)
    
    bfs = func(sx int, sy int) {
        q := make([][]int, 0)
        // 第一步：push起点
        q = append(q, []int{sx, sy})
        for len(q) > 0 {
            now := q[0]
            q = q[1:]
            x, y := now[0], now[1]
            // 扩展所有出边（四个方向）
            for i := 0; i < 4; i++ {
                nx := x + dx[i]
                ny := y + dy[i]
                // 任何时候访问数组前，判断合法性
                if nx < 0 || ny < 0 || nx >= m || ny >= n {
                    continue
                }
                if grid[nx][ny] == '1' && !visit[nx][ny] {
                    q = append(q, []int{nx, ny})
                    // BFS：入队时标记visit
                    visit[nx][ny] = true
                }
            }
        }
    }
    
    ans := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
             if grid[i][j] == '1' && !visit[i][j] {
                bfs(i, j)
                ans++
            }
        }
    }
    
    return ans;
};
```


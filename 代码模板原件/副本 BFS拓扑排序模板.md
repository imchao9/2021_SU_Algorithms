## C/C++代码模板

```c++
//C/C++
// LeetCode210 课程表II

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        n = numCourses;
        // 出边数组初始化，n个空list
        edges = vector<vector<int>>(n, vector<int>());
        inDeg = vector<int>(n, 0);
        for (vector<int>& pre : prerequisites) {
            int ai = pre[0];
            int bi = pre[1];
            // 加边模板
            addEdge(bi, ai);
        }
        auto ans = topsort();
        if (ans.size() < n) return {}; // 不能完成所有课程
        return ans;
    }

private:
    // 有向图找环 模板（拓扑排序）
    // 返回学的课程数
    vector<int> topsort() {
        vector<int> order;
        // 拓扑排序基于BFS，需要队列
        queue<int> q;
        // 从所有零入度点出发
        for (int i = 0; i < n; i++)
            if (inDeg[i] == 0) q.push(i);
        // 执行BFS
        while (!q.empty()) {
            int x = q.front(); // 取队头（这门课学了）
            q.pop();
            order.push_back(x);
            // 考虑x的所有出边
            for (int y : edges[x]) {
                inDeg[y]--; // 去掉约束关系
                if (inDeg[y] == 0) {
                    q.push(y);
                }
            }
        }
        return order;
    }

    void addEdge(int x, int y) {
        edges[x].push_back(y);
        inDeg[y]++;
    }

    int n;
    vector<vector<int>> edges;
    vector<int> inDeg; // in degree 入度
};
```

## 
## Java代码模板

```java
// Java
// LeetCode210 课程表II

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // 初始化
        n = numCourses;
        edges = new ArrayList<List<Integer>>();
        inDeg = new int[n];
        for (int i = 0; i < n; i++) {
           edges.add(new ArrayList<Integer>());
           inDeg[i] = 0;
        }
        // 建图，加边
        for (int[] pre : prerequisites) {
            int ai = pre[0];
            int bi = pre[1];
            addEdge(bi, ai);
        }
        // 拓扑排序
        return topsort();
    }

    int[] topsort() {
        int[] order = new int[n];
        int m = 0;
        Queue<Integer> q = new LinkedList<Integer>();
        // 零入度点入队
        for (int i = 0; i < n; i++)
            if (inDeg[i] == 0) q.offer(i);
        while (!q.isEmpty()) {
            Integer x = q.poll();
            order[m] = x;
            m++;
            // 扩展每个点
            for (Integer y : edges.get(x)) {
                inDeg[y]--;
                if (inDeg[y] == 0) q.offer(y);
            }
        }
        // n个课程都进出过队列，说明可以完成
        if (m == n) return order;
        return new int[0];
    }

    private void addEdge(int x, int y) {
        edges.get(x).add(y);
        inDeg[y]++;
    }

    private int n;
    private List<List<Integer>> edges;
    private int[] inDeg;
}
```

## Python代码模板

```python
# Python
# LeetCode210 课程表II

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 初始化
        self.n = numCourses
        self.edge = [[] for i in range(numCourses)]
        self.inDeg = [0] * numCourses
        # 加边
        for pre in prerequisites:
            ai, bi = pre[0], pre[1]
            self.addEdge(bi, ai)
        return self.topsort()

    def topsort(self):
        order = []
        q = deque()
        for i in range(self.n):
            if self.inDeg[i] == 0:
                q.append(i)
        while len(q) > 0:
            x = q.popleft()
            order.append(x)
            for y in self.edge[x]:
                self.inDeg[y] -= 1
                if self.inDeg[y] == 0:
                    q.append(y)
        if len(order) == self.n:
            return order
        return []

    def addEdge(self, u, v):
        self.edge[u].append(v)
        self.inDeg[v] += 1
```

## JavaScript代码模板

```javascript
// JavaScript
// LeetCode210 课程表II
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    var edge = [];
    var inDeg = [];
    for (let i = 0; i < numCourses; i++) {
        edge[i] = [];
        inDeg[i] = 0;
    }

    var addEdge = function(x, y) {
        edge[x].push(y);
        inDeg[y]++;
    }

    var topsort = function() {
        var q = [];
        var order = [];
        for (let i = 0; i < numCourses; i++)
            if (inDeg[i] == 0) q.push(i);
        while (q.length > 0) {
            let x = q.shift();
            order.push(x);
            for (const y of edge[x]) {
                inDeg[y]--;
                if (inDeg[y] == 0) q.push(y);
            }
        }
        if (order.length == numCourses) return order;
        return [];
    }

    for (const pre of prerequisites) {
        addEdge(pre[1], pre[0]);
    }
    return topsort();
};
```
## Golang代码模板

```go
//Go
// LeetCode210 课程表II

func topsort(outCome [][]int, inCome []int, numCourses int) {
	queue := make([]int,0)
	for i:=0; i<numCourses; i++ {
		if inCome[i] == 0 {
			queue = append(queue,i)
		}
	}
	rst := make([]int,0)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		rst = append(rst,node)
		for _,v := range outCome[node] {
			inCome[v]--
			if inCome[v] == 0 {
				queue = append(queue,v)
			}
		}
	}
	// 如果没有环，则认为是true
	if len(rst) == numCourses {
		return rst
	}

    return nil
}

func findOrder(numCourses int, prerequisites [][]int) []int {
	outCome := make([][]int,numCourses)
	inCome := make([]int,numCourses)

	// 有向图由pre[i][1] -> pre[i][0]
	for i:=0; i<len(prerequisites); i++ {
		outCome[prerequisites[i][1]] = append(outCome[prerequisites[i][1]],prerequisites[i][0])
		inCome[prerequisites[i][0]]++
	}

	return topsort(outCome, inCome, numCourses)
}

```



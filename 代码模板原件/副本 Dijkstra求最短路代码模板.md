## Python代码模板

```python
# Python
# https://www.acwing.com/problem/content/description/852/
from heapq import *

if __name__ == "__main__":
    n, m = map(int,input().split())
    
    ver = [[] for i in range(n + 1)] # 0~n
    edge = [[] for i in range(n + 1)] # 0~n
    dist = [1e9] * (n + 1)
    v = [False] * (n + 1)
    
    # 出边数组建图
    for i in range(m):
        x, y, z = map(int,input().split())
        ver[x].append(y)  # 另一端点
        edge[x].append(z) # 边权

    heap = []
    heappush(heap, (0, 1)) # (距离, 点)
    dist[1] = 0

    # Dijkstra 算法
    while heap:
        distance, x = heappop(heap)
        if v[x]:
            continue
        v[x] = True

        for i in range(len(ver[x])):
            y, z = ver[x][i], edge[x][i]
            if dist[y] > dist[x] + z:
                dist[y] = dist[x] + z
                heappush(heap, (dist[y], y))

    print(dist[n] if dist[n] != 1e9 else -1)
```

## C/C++代码模板

```c++
// C/C++
// https://www.acwing.com/problem/content/description/852/
#include<bits/stdc++.h>
using namespace std;
const int MAX_N = 150005, MAX_M = 150005;
vector<int> ver[MAX_N]; // 出边数组 - 另一端点
vector<int> edge[MAX_N]; // 出边数组 - 边权
int n, m, d[MAX_N];
bool v[MAX_N];
// pair<-dist[x], x>
priority_queue<pair<int, int>> q;

// 插入一条从x到y长度z的有向边
void add(int x, int y, int z) {
    ver[x].push_back(y);
    edge[x].push_back(z);
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        add(x, y, z);
    }
    memset(d, 0x7f, sizeof(d));
    d[1] = 0;
    q.push(make_pair(0, 1));
    while (!q.empty()) {
        int x = q.top().second;
        q.pop();
        if (v[x]) continue;
        v[x] = true;
        for (int i = 0; i < ver[x].size(); i++) {
            int y = ver[x][i], z = edge[x][i];
            if (d[y] > d[x] + z) {
                d[y] = d[x] + z;
                q.push(make_pair(-d[y], y));
            }
        }
    }
    if (d[n] == 0x7f7f7f7f) puts("-1");
    else cout << d[n] << endl;
}
```

## Java代码模板

```java
// Java
// https://www.acwing.com/problem/content/description/852/
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int m = input.nextInt();
        
        // 模板：出边数组初始化
        // 初态：[[], [], ... []]
        List<List<Integer>> ver = new ArrayList<List<Integer>>(); // 另一端点
        List<List<Integer>> edge = new ArrayList<List<Integer>>(); // 边权
        boolean[] v = new boolean[n + 1];
        int[] dist = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            ver.add(new ArrayList<Integer>());
            edge.add(new ArrayList<Integer>());
            v[i] = false;
            dist[i] = (int)1e9;
        }

        for (int i = 1; i <= m; i++) {
            int x = input.nextInt();
            int y = input.nextInt();
            int z = input.nextInt();
            // 出边数组 addEdge 模板
            ver.get(x).add(y);
            edge.get(x).add(z);
        }
        
        // Dijkstra算法
        dist[1] = 0;
        // 堆，每个结点是长度为2的数组 [点，dist]
        PriorityQueue<int[]> q = new PriorityQueue<>((a,b) -> {return a[1] - b[1];});
        q.offer(new int[]{1, 0});
        while(!q.isEmpty()){
            int[] top = q.poll();
            int x = top[0];
            if (v[x]) continue;
            v[x] = true;
            for (int i = 0; i < ver.get(x).size(); i++) {
                int y = ver.get(x).get(i);
                int z = edge.get(x).get(i);
                if (dist[y] > dist[x] + z) {
                    dist[y] = dist[x] + z;
                    q.offer(new int[]{y, dist[y]});
                }
            }
        }
        System.out.println(dist[n] == 1e9 ? -1 : dist[n]);
    }
}
```
   
## JavaScript代码模板

```javascript
/* JavaScript */
// https://www.acwing.com/problem/content/description/852/
class BinaryHeap {
    constructor() {
        // 数组存储完全二叉树
        // 从索引0开始存
        this.heap = [];
    }

    swap(i, j) {
        let temp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = temp;
    }

    isEmpty() {
        return this.heap.length == 0;
    }

    push(node) {
        // 插入到尾部
        this.heap.push(node);
        // 向上调整
        this.heapifyUp(this.heap.length - 1);
    }                

    pop() {
        let ans = this.heap[0];
        // 末尾交换到头部，然后删除末尾
        this.swap(0, this.heap.length - 1);
        this.heap.pop();
        // 向下调整
        this.heapifyDown(0);
        return ans;
    }

    heapifyUp(p) {        
        while (p > 0) {
            let fa = (p - 1) >> 1;  // 右移1位，等于整除2
            if (this.heap[p].key < this.heap[fa].key) { // 小根堆
                this.swap(p, fa);
                p = fa;
            }
            else break;
        }
    }

    heapifyDown(p) {
        let child = p * 2 + 1;
        while (child < this.heap.length) {  // child未出界，说明p有合法的child，还不是叶子
            let otherChild = p * 2 + 2;
            // 先比较两个孩子，谁小就继续跟p比较
            // child存较小的孩子
            if (otherChild < this.heap.length && this.heap[child].key > this.heap[otherChild].key)
                child = otherChild;
            // 让child跟p比较
            if (this.heap[p].key > this.heap[child].key) { // 小根堆
                this.swap(p, child);
                p = child;
                child = p * 2 + 1;
            }
            else break;
        }
    }
};

let n, m;
// 出边数组
let ver = []; // 另一端点
let edge = []; // 边权

let addEdge = (x, y, z) => {
    ver[x].push(y);
    edge[x].push(z);
}

// Dijkstra算法
let dijkstra = () => {
    let dist = [];
    let v = []
    for (let i = 1; i <= n; i++) {
        dist[i] = 1e9;
        v[i] = false;
    }
    dist[1] = 0;
    let q = new BinaryHeap();
    q.push({key: 0, vertex: 1}); // 距离作为key
    while (!q.isEmpty()) {
        let x = q.pop().vertex;
        if (v[x]) continue;
        v[x] = true;
        for (let i = 0; i < ver[x].length; i++) {
            let y = ver[x][i];
            let z = edge[x][i];
            if (dist[y] > dist[x] + z) {
                dist[y] = dist[x] + z;
                q.push({key: dist[y], vertex: y});
            }
        }
    }
    if (dist[n] === 1e9) return -1;
    return dist[n];
}

// 处理读入
let buf = '';
process.stdin.on('readable', function () {
    let chunk = process.stdin.read();
    if (chunk) buf += chunk.toString();
});
let getInputNums = line => line.split(' ').filter(s => s !== '').map(x => parseInt(x));
let getInputStr = line => line.split(' ').filter(s => s !== '');

process.stdin.on('end', function () {
    buf.split('\n').forEach(function (line, lineIdx) {
        if (lineIdx === 0) {
            n = getInputNums(line)[0];
            m = getInputNums(line)[1];
            for (let i = 1; i <= n; i++) {
                ver[i] = [];
                edge[i] = [];
            }
        } else if (lineIdx <= m) {
            let arr = getInputNums(line);
            let x = arr[0];
            let y = arr[1];
            let z = arr[2];
            addEdge(x, y, z);
            if (lineIdx === m) {
                console.log(dijkstra());
            }
        }
    });
});

```


## Golang代码模板

```go
// Go
// https://www.acwing.com/problem/content/description/852/

package main

import (
    "fmt"
)

type Pair struct {
    A, B int
}

type PriorityQueue struct {
    Data []Pair
}

func (q *PriorityQueue) Add (p Pair) {
    q.Data = append(q.Data, p)
    cur := len(q.Data) - 1
    for {
        if cur != 0 && q.Data[cur].A < q.Data[(cur - 1) / 2].A {
            q.Data[cur], q.Data[(cur - 1) / 2] = q.Data[(cur - 1) / 2], q.Data[cur]
            cur = (cur - 1) / 2
        } else {
            return
        }
    }
}

func (q *PriorityQueue) Pop() (res Pair) {
    res = q.Data[0]
    q.Data[0] = q.Data[len(q.Data) - 1]
    q.Data = q.Data[: len(q.Data) - 1]
    cur := 0
    for {
        l, r := cur * 2 + 1, cur * 2 + 2
        if l < len(q.Data) && q.Data[l].A < q.Data[cur].A && (r >= len(q.Data) || q.Data[l].A <= q.Data[r].A) {
            q.Data[cur], q.Data[l] = q.Data[l], q.Data[cur]
            cur = l
        } else if r < len(q.Data) && q.Data[r].A < q.Data[cur].A && (l >= len(q.Data) || q.Data[r].A <= q.Data[l].A) {
            q.Data[cur], q.Data[r] = q.Data[r], q.Data[cur]
            cur = r
        } else {
            return
        }
    }
}

const maxN = 150005

type Edge struct {
    V, W, Nxt int
}
var e = make([]Edge, maxN)
var head = make([]int, maxN)
var cnt = 1

func AddEdge(u, v, w int) {
    e[cnt].V = v
    e[cnt].W = w
    e[cnt].Nxt = head[u]
    head[u] = cnt
    cnt++
}

var n, m int
var dis = make([]int, maxN)
var q = PriorityQueue{Data: make([]Pair, 0)}

func main() {
    for i := range dis {
        dis[i] = -1
    }
    fmt.Scanf("%d %d", &n, &m)
    for ; m > 0; m-- {
        var u, v, w int
        fmt.Scanf("%d %d %d", &u, &v, &w)
        AddEdge(u, v, w)
    }
    dis[1] = 0
    q.Add(Pair{A: 0, B: 1})
    for len(q.Data) > 0 {
        cur := q.Pop()
        if cur.A != dis[cur.B] {
            continue
        } else if cur.B == n {
            break
        }
        for j := head[cur.B]; j != 0; j = e[j].Nxt {
            if dis[e[j].V] == -1 || cur.A + e[j].W < dis[e[j].V] {
                dis[e[j].V] = cur.A + e[j].W
                q.Add(Pair{A: dis[e[j].V], B: e[j].V})
            }
        }
    }
    fmt.Println(dis[n])
}
```


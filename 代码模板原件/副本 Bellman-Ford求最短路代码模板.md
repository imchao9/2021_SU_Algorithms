## Python代码模板

```python
# Python
# LeetCode 743
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [1e9] * (n + 1)
        dist[k] = 0
        for iteration in range(n - 1):
            updated = False
            for i in range(len(times)):
                x = times[i][0]
                y = times[i][1]
                z = times[i][2]
                if dist[y] > dist[x] + z:
                    dist[y] = dist[x] + z
                    updated = True
            if not updated:
                break
        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, dist[i])
        if ans == 1e9:
            ans = -1
        return ans
```

## C/C++代码模板

```c++
// C/C++
// LeetCode 743
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n + 1, 1e9);
        dist[k] = 0;
        for (int iteration = 1; iteration < n; iteration++) {
            bool updated = false;
            for (int i = 0; i < times.size(); i++) {
                int x = times[i][0];
                int y = times[i][1];
                int z = times[i][2];
                if (dist[y] > dist[x] + z) {
                    dist[y] = dist[x] + z;
                    updated = true;
                }
            }
            if (!updated) break;
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
            ans = max(ans, dist[i]);
        if (ans == 1e9) ans = -1;
        return ans;
    }
};
```

## Java代码模板

```java
// Java
// LeetCode 743
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        int[] dist = new int[n + 1];
        for (int i = 1; i <= n; i++) dist[i] = (int)1e9;
        dist[k] = 0;
        for (int iteration = 1; iteration < n; iteration++) {
            boolean updated = false;
            for (int i = 0; i < times.length; i++) {
                int x = times[i][0];
                int y = times[i][1];
                int z = times[i][2];
                if (dist[y] > dist[x] + z) {
                    dist[y] = dist[x] + z;
                    updated = true;
                }
            }
            if (!updated) break;
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
            ans = Math.max(ans, dist[i]);
        if (ans == 1e9) ans = -1;
        return ans;
    }
}
```
   
## JavaScript代码模板

```javascript
/* JavaScript */
// LeetCode 743
/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    dist = []
    for (let i = 1; i <= n; i++) dist[i] = 1e9;
    dist[k] = 0;
    for (let iteration = 1; iteration < n; iteration++) {
        let updated = false;
        for (let i = 0; i < times.length; i++) {
            let x = times[i][0];
            let y = times[i][1];
            let z = times[i][2];
            if (dist[y] > dist[x] + z) {
                dist[y] = dist[x] + z;
                updated = true;
            }
        }
        if (!updated) break;
    }
    let ans = 0;
    for (let i = 1; i <= n; i++)
        ans = Math.max(ans, dist[i]);
    if (ans == 1e9) ans = -1;
    return ans;
};
```

## Golang代码模板

```go
// LeetCode 743
func networkDelayTime(times [][]int, n int, k int) int {
    dist := make([]int, n + 1)
    for i := 1; i <= n; i++ {
        dist[i] = 1e9
    }
    dist[k] = 0;
    for iteration := 1; iteration < n; iteration++ {
        updated := false
        for i := 0; i < len(times); i++ {
            x := times[i][0]
            y := times[i][1]
            z := times[i][2]
            if dist[y] > dist[x] + z {
                dist[y] = dist[x] + z
                updated = true
            }
        }
        if !updated {
            break
        }
    }
    ans := 0
    for i := 1; i <= n; i++ {
        if ans < dist[i] {
            ans = dist[i]
        }
    }
    if ans == 1e9 {
        ans = -1
    }
    return ans
}
```


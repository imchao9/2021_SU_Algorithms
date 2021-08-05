class Solution {
    public int findCircleNum(int[][] isConnected) {
        DisjointSet s = new DisjointSet(isConnected.length);
        for (int i = 0; i < isConnected.length; i++)
            for (int j = 0; j < isConnected.length; j++)
                if (isConnected[i][j] == 1) s.unionSet(i, j);
        int ans = 0;
        for (int i = 0; i < isConnected.length; i++)
            if (s.find(i) == i) ans++;
        return ans;
    }

class DisjointSet {
    public DisjointSet(int n) {
        fa = new int[n];
        for (int i = 0; i < n; i++) fa[i] = i;
    }

    public int find(int x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }

    public void unionSet(int x, int y) {
        x = find(x);
        y = find(y);
        if (x != y) fa[x] = y;
    }

    int[] fa;
};
}
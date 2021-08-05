class DisjointSet {
public:
    DisjointSet(int n) {
        fa = vector<int>(n, 0);
        for (int i = 0; i < n; i++) fa[i] = i;
    }

    int find(int x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }

    void unionSet(int x, int y) {
        x = find(x), y = find(y);
        if (x != y) fa[x] = y;
    }

private:
    vector<int> fa;
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        DisjointSet s(isConnected.size());
        for (int i = 0; i < isConnected.size(); i++)
            for (int j = 0; j < isConnected.size(); j++)
                if (isConnected[i][j] == 1) s.unionSet(i, j);
        int ans = 0;
        for (int i = 0; i < isConnected.size(); i++)
            if (s.find(i) == i) ans++;
        return ans;
    }
};
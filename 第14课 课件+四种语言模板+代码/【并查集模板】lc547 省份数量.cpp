class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        // 建立并查集
        for (int i = 0; i < isConnected.size(); i++)
            fa.push_back(i);
        // 每条边代表一次合并
        for (int i = 0; i < isConnected.size(); i++)
            for (int j = i + 1; j < isConnected.size(); j++)
                if (isConnected[i][j] == 1) { 
                    unionSet(i, j);
                }
        // 有几棵树？（有几个根）
        int ans = 0;
        for (int i = 0; i < isConnected.size(); i++)
            if (find(i) == i) ans++;
        return ans;
    }

private:
    void unionSet(int i, int j) {
        int x = find(i);
        int y = find(j);
        if (x != y) fa[x] = y;
    }

    int find(int x) {
        if (x == fa[x]) return x;
        return fa[x] = find(fa[x]);
    }

    vector<int> fa;
};
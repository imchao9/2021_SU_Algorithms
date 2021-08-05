class DisjointSet {
    constructor(n) {
        this.fa = [];
        for (let i = 0; i < n; i++) this.fa[i] = i;
    }

    find(x) {
        if (x == this.fa[x]) return x;
        return this.fa[x] = this.find(this.fa[x]);
    }

    unionSet(x, y) {
        x = this.find(x);
        y = this.find(y);
        if (x != y) this.fa[x] = y;
    }
};
/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function(isConnected) {
        let s = new DisjointSet(isConnected.length);
        for (let i = 0; i < isConnected.length; i++)
            for (let j = 0; j < isConnected.length; j++)
                if (isConnected[i][j] == 1) s.unionSet(i, j);
        let ans = 0;
        for (let i = 0; i < isConnected.length; i++)
            if (s.find(i) == i) ans++;
        return ans;
};
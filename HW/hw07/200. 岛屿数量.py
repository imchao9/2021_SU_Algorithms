class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            方法2: 并查集
            思路：这题用并查集就很好做了，这就是再问how many disjointed set do we have
        """
        # 这题的坑就是：要把所有水的区域都划到同一个set，要不最后结果不对
        row, col = len(grid), len(grid[0])
        self.row, self.col = row, col
        self.fa = [-1 for i in range(row*col+1)]
        for i in range(row):
            for j in range(col):
                self.fa[self.encoder(i, j)] = self.encoder(i, j)
        self.fa[row*col] = -1  # 都是水的区域
        print(self.fa)
        self.dx = [1, 0, -1, 0]
        self.dy = [0, 1, 0, -1]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "0":
                    self.unionSet(self.encoder(i, j), row*col)
                for k in range(4):
                    ni = self.dx[k] + i
                    nj = self.dy[k] + j
                    if ni < 0 or nj < 0 or ni >= row or nj >= col:
                        continue
                    elif grid[ni][nj] == grid[i][j]:
                        if grid[ni][nj] == "0":
                            self.unionSet(self.encoder(ni, nj), row*col)
                        else:
                        # self.fa[self.find(self.encoder(i, j))] = self.find(self.encoder(ni, nj))
                            self.unionSet(self.encoder(i, j), self.encoder(ni, nj))
        print(self.fa)
        # Count the number of disjointed set
        ans = 0
        for i in range(row):
            for j in range(col):
                if self.find(self.encoder(i, j)) == self.encoder(i, j):
                    ans += 1
        return ans
    
    # Convert 2D table to 1D array
    def encoder(self, i, j):
        if i==self.row and j==self.col:
            return self.row * self.col
        return i * self.col + j  # 这里必须*col, 因为你每次都是以 i * col 为终点，重新开始下一个row的计数

    def find(self, x):
        if self.fa[x] == x:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def unionSet(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.fa[root_x] = root_y
        
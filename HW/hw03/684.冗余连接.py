class Solution:
    def findRedundantConnection(self, input: List[List[int]]) -> List[int]:
        # 这里面不知道有多少个节点，所以要循环一边来找
        # 出现过的最大的点就是n
        num_nodes = 0
        for edge in input:
            u = edge[0]
            v = edge[1]
            num_nodes = max(u, num_nodes)
            num_nodes = max(v, num_nodes)

        # 模板：出边数组初始化
        # 初态：n+1 个empty list, [[], [], ... []]
        self.edges = [[] for i in range(num_nodes+1)]   # Why 'range(num_nodes+1)'? ==> Because 节点值是从1,2,...,N, need extra spot for indexing N
        # 初态：n+1 个boolean, [False, False, ..., False]
        self.visited = [False for i in range(num_nodes+1)] 
        self.hasCycle = False 

        # 给无向图加边: 无向图里，每一条边都是双向的
        for edge in input:
            node1, node2 = edge[0], edge[1]
            self.addEdge(node1, node2)
            self.addEdge(node2, node1)
            # 每加一条边，check看看是否多了环
            self.dfs(node1, -1) # 从点1开始，-1是因为1是开始点，他没有父亲
            if self.hasCycle:
                return edge
        return []


    def addEdge(self, x: int, y: int):
        self.edges[x].append(y)

    # 这题的重点就是如何用dfs来找环
    # 通过深度遍历来找环: 从任意一个点出发去找环. 这需要一个visited 数组，来避免重新访问
    # 通过dfs，会产生一颗搜索树，
    def dfs(self, x: int, fa: int):
        # 第一步，标记已访问
        self.visited[x] = True
        # 第二步：遍历出所有边
        for y in self.edges[x]:
            # print(f"y: {y}")
            if y == fa:
                continue    # 返回父亲，这不是环
            if self.visited[y]:
                self.hasCycle = True
            else:
                self.dfs(y, x)  # 递归找环，且定义x是y的father
        # 第三步，还原共享变量
        self.visited[x] = False



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
            方法：并查集
            思路：因为并查集里是不能有环的。一开始所有的节点都是单独一个 disjointed set。把每个节点都遍历一遍，如果他两指一条边的，那就放在一起。
            在union的时候，如果发现，the two nodes that we want to union have unioned already, then return that edges as result
        """
        # 并查集初始化
        n = len(edges)
        self.fa = [i for i in range(n+1)]

        # 把每个edge 都遍历一遍
        # for i in range(n):
        #     for j in range(i+1, n):
        #         pass

        self.ans = []
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            self.unionSet(node1, node2)

        return self.ans
    
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
        else:
            self.ans = [x, y]



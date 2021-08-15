

# Minimum Spanning Tree(最小生成树)

## ***What is Minimum Spanning Tree(最小生成树)?*** 

A *minimum spanning tree (MST)* or minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree. – https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

A single graph can have many different spanning trees, but we want the one that has the minimum sum of weight given to each edge of the spanning tree. If we want to find this manually, then we have to list out all possible spanning tree. 

![image-20210813005333498](img/image-20210813005333498.png)

Imaging if we have a graph with 6 vertice and 7 edge amount then, then that would take C(7, 5) = 7! / (5! * (7-5)! ) = 7 * 6 / 2 = 21 

![image-20210813005238357](img/image-20210813005238357.png)

==> this can be pretty cumbersom and time-comsuming ==> So, here are two algoirthm that can help use to find MST: 1) Kruskal algorithm, and 2) Prim’s Algorithm

(picture taken from this video, https://www.youtube.com/watch?v=4ZlRH0eK-qQ&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=44)

Properties:

- MST is a type of greedy algorithm, with O(E^2) time complexity
- Used for undirected graph
- Return a subgraph that with (V-1) edge
- 对DP方也可以找出MST（当然，所有greedy algo能做的，DP都可以）。但是greedy algo的效率更高。但麻烦的一点就是greedy algo不保证正确性，所以在使用之前必须要证明他能给出optimal solution.  这题的具体证明可以看这里，[Introduction to Algorithms 6.046J/18.401J - LECTURE 16 Greedy Algorithms (and Graphs)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-16-greedy-algorithms-minimum-spanning-trees/lec16.pdf) 或者我cse2331的笔记，https://drago1234.github.io/Knowledge_Bank/docs/2019_fall/cse2331/scanned_file/13_MST_and_Shortest_path.pdf

MST Optimalism Proof

![image-20210812234841885](img/image-20210812234841885.png)

## Kruskal MST Algorithm

**Kruskal MST Algorithm** – ==Always selected the minimum weighted edge amount all unvisited_set, that’s min(Edge<vi, vj>), that doesn’t form a cycle==



![image-20210813010707695](img/image-20210813010707695.png)



Some Properties:

- Work for disjointed graph –> It will find the MST for each graph.



**Time Complexity:**

![image-20210813012405117](img/image-20210813012405117.png)

– Reference, [MIT Algorithm](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-16-greedy-algorithms-minimum-spanning-trees/lec16.pdf)

**具体实现：**

Krustal Algorithm often is implemented with disjoined-set, here is a python version, https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

- Adjacent List: O(V^2)
- Disjointed union: O(E logV)



## Prim’s MST Algorithm

**Prim’s MST Algorithm:** ==Always selected the edge that has minimum weight between MST set and unvisited_set, that’s min( (U - G.V), U), where U is the unvisited_set and is initialized as (G.V - v1), and (U - G.V) is the MST that we need to construct.==

![image-20210813011021968](img/image-20210813011021968.png)

- start with empty tree
- Maintain two set of vertices: 1) a set of vertices that already included in MST (aka explored_set, visited_set, or MST_set); 2) contains a set of vertices that has not yet included.
- Consider all edges connect two set, and picks the minimum weighted edge, and move the endpoint of the edge to the first set that containing MST



**Time Complexity:**

![](img/image-20210813012256468.png)

![image-20210813012317900](img/image-20210813012317900.png)

– Reference, [MIT Algorithm](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-16-greedy-algorithms-minimum-spanning-trees/lec16.pdf)



**具体实现：**

- Adjacent list:  ==>  

There is a Python version, that use adjacent list to implement it, link here, https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/ 

```text
# G is graph, G.V = set of vertices of graph G, 
procedure PrimMST(G):
	U= G.V - {v1}	# let U be all the vertices that hasn't visited yet
	v1.MSTparent = Null	# let's the parent of root to be None 
	while U!=0 and there is an edge from (G.V - U) to U:	# while there is an vertices that we hasn't visited and there exist a path from explored world to that edge
		(vi, vj) = minimum weight edge from (G.V - U) to U	# Find the lowest cost path, and visited it
		vj.MSTparent = vi	# add to the explored world
		U = U - {vj}		# remove that vertices from queue/stack
	end while
	

# m = number of vertices of G
# n = number of edges of G
# Time Complextity: O(n^2 + m) = O(n^2)
```

- with Fibonacci heap
- With priority Queue, or binary heap

**Psudocode:**

![image-20210813012205404](img/image-20210813012205404.png)

![image-20210812235110603](img/image-20210812235110603.png)

(Watch this video if you still don’t understand,)

**Reference:** 

- Prim’s Minimum Spanning Tree (MST) | Greedy Algo-5, https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
- Kruskal’s Minimum Spanning Tree Algorithm | Greedy Algo-2, https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
- YouTube Video,  [3.5 Prims and Kruskals Algorithms - Greedy Method](https://www.youtube.com/watch?v=4ZlRH0eK-qQ&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=44)
- MIT Course Slide, [Introduction to Algorithms 6.046J/18.401J - LECTURE 16 Greedy Algorithms (and Graphs)](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/video-lectures/lecture-16-greedy-algorithms-minimum-spanning-trees/lec16.pdf) 



# Shortest Paths

## Bellman–Ford Algorithm

- Bellman-Ford is a type of DP algorithm, with O(VE) of time complexity 
- Goal: Given a graph and a source vertex *src* in graph, find shortest paths from *src* to all vertices in the given graph.
- Property:
  - allow the graph contain negative weighted edge
- Th





Reference:

- Bellman–Ford Algorithm | DP-23, https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/



## Dijkstra’s shortest path algorithm

- Dijkstra’s algorithm is a Greedy algorithm and time complexity is O(V+E LogV), where V is number of vertices, and E is the number of edges
- Dijkstra doesn’t work for Graphs with negative weight edges



**Algorithm** 
Following are the detailed steps.
***Input:*** Graph and a source vertex *src* 
***Output:*** Shortest distance to all vertices from *src*. If there is a negative weight cycle, then shortest distances are not calculated, negative weight cycle is reported.
**1)** This step initializes distances from the source to all vertices as infinite and distance to the source itself as 0; ==> Create an array dist[] of size |V| with all values as infinite except dist[src] where src is source vertex.
**2)** This step calculates shortest distances. Do following |V|-1 times where |V| is the number of vertices in given graph. 
…..**a)** Do following for each edge u-v 
………………If dist[v] > dist[u] + weight of edge uv, then update dist[v] 
………………….dist[v] = dist[u] + weight of edge uv
**3)** This step reports if there is a negative weight cycle in graph. Do following for each edge u-v 
……If dist[v] > dist[u] + weight of edge uv, then “Graph contains negative weight cycle” 
The idea of step 3 is, step 2 guarantees the shortest distances if the graph doesn’t contain a negative weight cycle. If we iterate through all edges one more time and get a shorter path for any vertex, then there is a negative weight cycle

***How does this work?*** Like other Dynamic Programming Problems, the algorithm calculates shortest paths in a bottom-up manner. It first calculates the shortest distances which have at-most one edge in the path. Then, it calculates the shortest paths with at-most 2 edges, and so on. After the i-th iteration of the outer loop, the shortest paths with at most i edges are calculated. There can be maximum |V| – 1 edges in any simple path, that is why the outer loop runs |v| – 1 times. The idea is, assuming that there is no negative weight cycle, if we have calculated shortest paths with at most i edges, then an iteration over all edges guarantees to give shortest path with at-most (i+1) edges (Proof is simple, you can refer [this](http://courses.csail.mit.edu/6.006/spring11/lectures/lec15.pdf) or [MIT Video Lecture](http://www.youtube.com/watch?v=Ttezuzs39nk))

Reference: 

- Dijkstra’s shortest path algorithm | Greedy Algo-7, https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/







# Summary:

- MST(minimum spanning tree, or 最小生成树): 这个找的是所有spanning tree 里，the one with the minimum sum of weight. 要考虑整条path上edge的weight, or cost， 所以可以用greedy的思路来实现。
  - **Kruskal MST Algorithm** – ==Always selected the minimum weighted edge amount all unvisited_set, that’s min(Edge<vi, vj>), that doesn’t form a cycle==
  - **Prim’s MST Algorithm:** ==Always selected the edge that has minimum weight between MST set and unvisited_set, that’s min( (U - G.V), U), where U is the unvisited_set and is initialized as (G.V - v1), and (U - G.V) is the MST that we need to construct.==
- Shortesting path: 这个考虑的是任意一点到起点的最短距离， 所以必须要用DP的思路来实现
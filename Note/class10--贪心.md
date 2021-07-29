

[TOC]

# Outline

- 贪心理论与常见的证明方法
- 贪心题目实战



# 贪心算法知识点

- 在每一步选择中，都采取在当前状态下的最有决策(**局部最优)**， 但我们希望由此导致的最终结果是全局最优的
- 他与只有要讲的动态规划相比，不同之处在于：他<u>不对整个状态空间遍历搜索</u>，而是始终按照局部最优的选择方法，执行下去，不回头（就有点像dfs，只要找当前path的最优解) ==> 正因为这个特性，贪心算法<u>不一定能得到正确的结果</u> 
- 但为什么还要讲贪心算法呢？ ==》因为它不考虑未来，所以<u>效率高</u>，有一些场景可能会比较实用。就像人一样，我们做得每个决定不会有太多时间去想的，谁知道未来，都是考虑当前状态的最决战，所以我们做得很多决定都不可能是全局最优的



# 贪心实战例题

#### 

## [零钱兑换](https://leetcode-cn.com/problems/coin-change/)（Medium）

- [零钱兑换](https://leetcode-cn.com/problems/coin-change/)（Medium）半年内出题频次：

| Facebook | 字节跳动 | 微软 | Amazon |
| :------: | :------: | :--: | :----: |
|    4     |    11    |  14  |   12   |

| 高盛集团 | 百度 | Google | 腾讯 |
| :------: | :--: | :----: | :--: |
|    4     |  2   |   6    |  8   |

| Bloomberg | Apple |
| :-------: | :---: |
|     6     |   4   |

Question:

![image-20210729022502164](img/image-20210729022502164.png)

Idea:

![image-20210729022633530](img/image-20210729022633530.png)

![image-20210729022646755](img/image-20210729022646755.png)



Python Code:

```python
```







## [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)（Easy）

- [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)（Easy）半年内出题频次：

| 华为 |
| :--: |
|  4   |

Question:



Idea:



Python Code:

```python

```





## [分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)（Easy）

- [分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)（Easy）半年内出题频次：

| 字节跳动 |
| :------: |
|    3     |

Question:



Idea:



Python Code:

```python

```



## [买卖股票的最佳时机 II ](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)（Easy）

- [买卖股票的最佳时机 II ](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)（Easy）半年内出题频次：

| 字节跳动 | Amazon | 高盛集团 | Apple |
| :------: | :----: | :------: | :---: |
|    9     |   16   |    2     |   4   |

Question:



Idea:



Python Code:

```python

```





## [跳跃游戏 II ](https://leetcode-cn.com/problems/jump-game-ii/)（Medium）

- [跳跃游戏 II ](https://leetcode-cn.com/problems/jump-game-ii/)（Medium）半年内出题频次：

| Facebook | 字节跳动 | 华为 | Amazon |
| :------: | :------: | :--: | :----: |
|    2     |    10    |  86  |   16   |

| 阿里巴巴 | 百度 | Apple |
| :------: | :--: | :---: |
|    3     |  2   |   4   |

Question:



Idea:



Python Code:

```python

```





## [完成所有任务的最少初始能量](https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks/)（Hard）

- [完成所有任务的最少初始能量](https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks/)（Hard）半年内出题频次：

| eBay |
| :--: |
|  2   |

Question:



Idea:



Python Code:

```python

```




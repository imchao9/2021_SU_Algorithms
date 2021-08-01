"""
动态规划思路：因为n是正整数，所以不应该从0开始，我们也不需要去想opt[0]是什么

1) 确定dp数组以及下标的含义: dp[i] represent the number to way to get to i step of stair
2) 确定递推公式: 
For solving dp[i], we only need to consider the solution for dp[i-1] and dp[i-2], and in this problem, their sum will be the result. 为啥是他们的和呢？ ==》 因为只有这两条路径可以走。
dp[i] = dp[i - 1] + dp[i - 2]

3）dp数组如何初始化
i为0，dp[i]应该是多少呢，这个可以有很多解释，但都基本是直接奔着答案去解释的。==》 但其实我们不需要去关心跑到第0层的答案，因为题目说了，n的范围是正整数，就不会出现n，所以不用考虑dp[0]如果初始化，只初始化dp[1] = 1，dp[2] = 2，然后从i = 3开始递推，这样才符合dp[i]的定义。
4）确定遍历顺序
从递推公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，遍历顺序一定是从前向后遍历的
5）举例推导dp数组：
举例当n为5的时候，dp table（dp数组）应该是这样的
dp =    [inf, 1, 2, 3, 5, 8]
index=        1  2  3  4  5
如果代码出问题了，就把dp table 打印出来，看看究竟是不是和自己推导的一样。
Note：其实这就是斐波那契数列 
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # record the best answer from 0 to n (total is n+1 element)
        if n <= 2:
            return n
        opt = [float("inf")] * (n+1)
        opt[1] = 1
        opt[2] = 2
        for i in range(3, n+1):
            opt[i] = opt[i-1] + opt[i-2]
        print(opt)
        return opt[n]

# Good Reference: https://leetcode-cn.com/problems/climbing-stairs/solution/dai-ma-sui-xiang-lu-dong-tai-gui-hua-jin-y1hw/
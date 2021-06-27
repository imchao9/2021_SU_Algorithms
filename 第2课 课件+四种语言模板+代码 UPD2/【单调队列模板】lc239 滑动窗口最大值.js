/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
    var ans = [];
    // 数组模拟双端队列，存下标（代表时间）
    var l = 0, r = -1; // left, right
    var q = []; // left~right（包含两端）存储队列中的元素
    for (let i = 0; i < nums.length; i++) {
        // 保证队头合法性
        while (l <= r && q[l] <= i - k) l++;
        // 维护队列单调性，插入新的选项
        while (l <= r && nums[q[r]] <= nums[i]) r--;
        r++;
        q[r] = i;
        // 取队头更新答案
        if (i >= k - 1) ans.push(nums[q[l]]);
    }
    return ans;
};
/*
1 3 [-1 -3 5] 3 6 7

时间：expire_time(-1) < expire_time(-3) < expire_time(5)
值大小：-1 < -3 < 5
求max

冗余：一个下标i一个下标j，如果i<j，并且nums[i]<=nums[j]，i是冗余
去除冗余：维护下标（时间）递增、nums递减（>=）的队列
队头最优，随着下标增长，队头expire后，后面的开始逐渐变成最优
*/
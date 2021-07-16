/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let ans = [];
    // 开始位置（lower_bound）：查询第一个>=target的数
    // 范围 [0 .. n-1 ] + [n表示不存在]
    let left = 0, right = nums.length;
    while (left < right) {
        let mid = (left + right) >> 1;
        if (nums[mid] >= target) right = mid;
        else left = mid + 1;
    }
    ans[0] = right;  //第一个>=target的数的下标（不存在为n）

    // 结束位置：查询最后一个<=target的数
    // 范围 [-1表示不存在] + [0 .. n-1 ]
    left = -1; right = nums.length - 1;
    while (left < right) {
        let mid = (left + right + 1) >> 1;
        if (nums[mid] <= target) left = mid;
        else right = mid - 1;
    }
    ans[1] = right; //最后一个<=target的数（不存在为-1）

    // target出现在[ans[0], ans[1]]
    if (ans[0] > ans[1]) ans = [-1, -1];
    return ans;
};
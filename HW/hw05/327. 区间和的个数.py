class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0

        sum_list = nums[:]
        for index in range(1, len(nums)):
            sum_list[index] += sum_list[index - 1]
        
        return self.mergeSort(0, len(nums) - 1, lower, upper, sum_list)

    def mergeSort(self, l, r, lower, upper, sum_list):
        if l == r:
            if sum_list[l] >= lower and sum_list[l] <= upper:
                return 1
            return 0

        mid = (l + r) // 2
        res = self.mergeSort(l, mid, lower, upper, sum_list) + self.mergeSort(mid + 1, r, lower, upper, sum_list)

        merge_pos = lower_pos = upper_pos = mid + 1
        tmp_list = []
        for index in range(l, mid + 1):
            while merge_pos <= r and sum_list[merge_pos] < sum_list[index]:
                tmp_list.append(sum_list[merge_pos])
                merge_pos += 1
            while lower_pos <= r and sum_list[lower_pos] - sum_list[index] < lower:
                lower_pos += 1
            while upper_pos <= r and sum_list[upper_pos] - sum_list[index] <= upper:
                upper_pos += 1
            
            res += upper_pos - lower_pos
            tmp_list.append(sum_list[index])

        for index in range(len(tmp_list)):
            sum_list[l + index] = tmp_list[index]

        return res
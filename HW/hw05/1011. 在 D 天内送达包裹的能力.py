class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 思路：看到这种求最值的问题，第一个想到的就是用二分法，将最优解问题转化成判定问题，然后切割解空间，寻找答案
        left, right = max(weights), sum(weights) # l define the lower bound of weight limit, where one day per package; and right index defines the upper bound of weight limit, where all package get delivered within one day.
        while left < right:
            mid = (left + right)//2
            # if 'mid' is within the limit, that means anything greater than mid will also valid ==> here, our goal is to find the first one(weight limit) that is valid
            if self.isWithinLimit(weights, days, mid): 
                right = mid
            else:
                left = mid + 1
        
        return right

    # [1,2,3,1,1], D = 4  l, r = 3, 8, Limit = (l+r)//2 = 5
    # [1, 2] [3, 1, 1]
    # 
    # Can we send out all the package with in D days, with weight limit of W?
    def isWithinLimit(self, weights: List[int], days: int, limit: int) -> bool:
        # if len(weights) == 0:
        #     return True
        # day_counter = 1 # Now, we know there is at least one package
        day_counter = 0
        groupSum = 0
        for i in range(len(weights)):
            if i == 0:  # For the first day
                day_counter = 1
            if groupSum + weights[i] <= limit:
                groupSum += weights[i]
            else:   # Overloaded, need to start a new group
                groupSum = weights[i]
                day_counter += 1
        
        return day_counter<=days
        
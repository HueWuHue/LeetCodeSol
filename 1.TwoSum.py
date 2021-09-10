class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in values:
                return [i, values[remaining]] # Return Ans
            else:
                values[num] = i # Store Value as Key and Index as Value

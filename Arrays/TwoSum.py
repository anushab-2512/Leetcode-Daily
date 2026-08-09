 """
        LeetCode :Two Sum
        Difficulty: Easy

        Approach:
        Store each number and its index in a dictionary.
        For every number, check whether its complement
        (target - num) was already seen.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen ={}
        for i , num in enumerate(nums):
            n=target-num
            if n not in seen :
                seen [num]=i
            else:
                return [seen [n],i]
       

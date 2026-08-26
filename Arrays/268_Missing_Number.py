class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        total_sum=(n*(n+1))//2
        actual_sum=sum(nums)
        missing_value=total_sum - actual_sum
        return missing_value

# Time Complexity: O(n),  because we calculate the sum of all elements. 
# Space Complexity: O(1), because we use only constant extra space.

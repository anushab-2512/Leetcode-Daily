"""
  Intuition
        The goal is to find the index at which a target value should be inserted in a sorted array nums so that the order is maintained. 
        If the target is already present, return its index. 
        Otherwise, return the position it would be inserted to keep the list sorted.

  Approach
        Linear Search: Iterate through the array to check if the target exists. If found, return the index.

        Backward Search: If not found, traverse from the end to find the first element less than the target, and return its index + 1.

        Edge Case Handling: Explicit checks for arrays of size 1, although these checks are redundant due to earlier loops.

  Complexity
        Time complexity: O(n)
        Because we are scanning the array once in a forward loop and potentially again in a backward loop.
        Space complexity: O(1)
        Only a few variables are used for indexing, no extra space is
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        mid=0
        while start<=end:
            mid=start+(end-start)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            else:
                end=mid-1
        return start

        

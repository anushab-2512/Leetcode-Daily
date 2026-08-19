# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        total_num=len(nums)
        if not total_num:
            return None
        mid_node=total_num//2
        return TreeNode(
            nums[mid_node],
            self.sortedArrayToBST(nums[:mid_node]),self.sortedArrayToBST(nums[mid_node + 1 :])
        )

"""
Method: recursion

Since nums is a sorted list, the middle element nums[len(nums)//2] must be the root node of nums.
Thus, after setting the middle element be the root, finding the middle element in the left subarry nums[:len(nums)//2] and right subarry nums[len(nums)//2 + 1 : ]
"""

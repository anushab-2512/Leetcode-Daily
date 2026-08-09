"""
Intuition
We need to find three numbers whose sum is closest to the target. Sorting the array allows us to efficiently adjust the sum using two pointers instead of checking every possible triplet.

Approach
-Sort the array.
-Iterate through each element as the first number.
-Use two pointers (left and right) to find the closest sum with the remaining elements.
-Update the closest sum whenever a better candidate is found.
-If the current sum equals the target, return it immediately since no closer sum is possible.

Complexity
Time complexity:
O(n2)

Space complexity:
O(1)
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return target

        return closest

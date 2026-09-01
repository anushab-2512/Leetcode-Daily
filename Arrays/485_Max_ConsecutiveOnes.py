class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_count is initialized to keep track of the maximum count of consecutive ones
        max_count=0 
        # cuu_count to keep track of the cuurent count of consecutive ones
        curr_count=0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_count+=1
                max_count=max(max_count,curr_count)
            else:
                curr_count=0
        return max_count


      # another approch
        
        # maxi = result = 0
        
        # for num in nums:
        #     if num == 1:
        #         result += 1
        #         maxi = max(maxi, result)
        #     else:
        #         result = 0
        # return maxi

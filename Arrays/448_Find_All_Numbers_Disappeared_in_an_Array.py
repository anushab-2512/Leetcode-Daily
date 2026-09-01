class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=[]
        numbers=set(nums)
        for n in range(1,len(nums)+1):
            if n not in numbers:
                seen.append(n)
        return seen

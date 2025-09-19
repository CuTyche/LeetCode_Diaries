class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k = 1
        for num in nums:
            if num> 0 and k == num:
                k+=1
        return k
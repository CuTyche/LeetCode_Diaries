class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod, zero_cnt = 1, 0
        
        # compute product of non-zero elements & count zeros
        for x in nums:
            if x == 0:
                zero_cnt += 1
            else:
                prod *= x
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt > 1:
                res[i] = 0
            elif zero_cnt == 1:
                res[i] = prod if c == 0 else 0
            else:  # zero_cnt == 0
                res[i] = prod // c
        return res

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        res = []

        for key in count:
            if count[key] > len(nums)//3:
                res.append(key)
        return res
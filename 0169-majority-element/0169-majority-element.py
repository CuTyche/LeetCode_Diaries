class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = Counter(nums)
        for num, freq in count.items():
            if freq > n//2:
                return num
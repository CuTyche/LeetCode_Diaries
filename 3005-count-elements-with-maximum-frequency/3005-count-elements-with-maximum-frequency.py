class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_count = max(freq.values())
        return sum(v for v in freq.values() if v == max_count)
        
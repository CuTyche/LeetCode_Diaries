class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        max_count = max(freq.values())
        return sum(count for count in freq.values() if count == max_count)
        
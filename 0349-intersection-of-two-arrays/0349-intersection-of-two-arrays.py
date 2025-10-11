class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        n = Counter(nums1)
        m = Counter(nums2)
        
        common = n & m
        return list(set(common.elements()))
        
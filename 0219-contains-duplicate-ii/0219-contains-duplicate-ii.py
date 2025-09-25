class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for l in range(len(nums)):
            for r in range(l+1, min(len(nums), l+k+1)):
                if nums[l] == nums[r]:
                    return True
        return False
        
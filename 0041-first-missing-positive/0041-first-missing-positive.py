class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n:  # only work with valid numbers
                index = nums[i] - 1
                if nums[i] != nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    continue   # recheck the swapped value
            i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

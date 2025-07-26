class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums2 = []
        for n in nums:
            if n == val:
                continue
            nums2.append(n)
        for i in range(len(nums2)):
            nums[i] = nums2[i]
        return len(nums2)
        
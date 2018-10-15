class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in range(len(nums) - 1, -1, -1):
            if n:
                if nums[n] == nums[n - 1]:
                    nums.pop(n)

        return len(nums)

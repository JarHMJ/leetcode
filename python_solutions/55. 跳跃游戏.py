from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0
        for n in range(len(nums) - 1):
            current = max(current - 1, nums[n])
            if current == 0:
                return False
        return True

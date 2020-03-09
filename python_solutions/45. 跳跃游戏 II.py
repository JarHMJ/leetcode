from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_max_index = 0
        pre_max_index = 0
        count = 0
        for i, v in enumerate(nums[:-1]):
            if cur_max_index == i:
                if pre_max_index > i + v:
                    cur_max_index = pre_max_index
                else:
                    pre_max_index = cur_max_index = i + v
                count += 1
            else:
                pre_max_index = max(pre_max_index, i + v)

        return count

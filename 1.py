class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [num_dict[target - nums[i]], i]
            num_dict[nums[i]] = i


if __name__ == '__main__':
    test = Solution()
    print(test.twoSum([3, 3], 6))

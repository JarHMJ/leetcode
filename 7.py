class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        nums = list(str(x))
        if nums[0] == '-':
            new_nums = nums[::-1]
            new_nums.pop()
            print(new_nums)
            new_nums = ['-'] + new_nums
        else:
            new_nums = nums[::-1]
        result = int(''.join(new_nums))
        if result < -(2 ** 31) or result > 2 ** 31 - 1:
            result = 0
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.reverse(-123))

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count


if __name__ == '__main__':
    test = Solution()
    print test.NumberOf1(-1)

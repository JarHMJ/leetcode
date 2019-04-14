# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            pre = 0
            result = 1
            for _ in range(n - 1):
                result, pre = pre + result, result
            return result


if __name__ == '__main__':
    test = Solution()
    print test.Fibonacci(6)

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            pre = 1
            result = 2
            for _ in range(number - 2):
                pre, result = result, pre + result
            return result

if __name__ == '__main__':
    test = Solution()
    print test.jumpFloor(5)


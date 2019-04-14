# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <=0:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            pre = 1
            result = 2
            for _ in range(number - 2):
                pre, result = result, pre + result
            return result
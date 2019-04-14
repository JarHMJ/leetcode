# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        else:
            return 2 ** (number - 1)

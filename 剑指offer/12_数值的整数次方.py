# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        flag = 0
        if exponent < 0:
            flag = 1
            exponent = -exponent

        result = 1
        for _ in range(exponent):
            result *= base

        if flag:
            result = 1.0 / result
        return result

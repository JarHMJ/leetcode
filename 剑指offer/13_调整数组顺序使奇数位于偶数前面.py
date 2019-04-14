# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        return sorted(array, key=lambda x: x % 2 == 0)

if __name__ == '__main__':
    test = Solution()
    print test.reOrderArray([1,2,3,4,5,6,7])
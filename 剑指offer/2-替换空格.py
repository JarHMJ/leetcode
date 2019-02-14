# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        length = len(s)
        new_s = []
        for i in range(length):
            if s[i] == ' ':
                new_s.append('%20')
            else:
                new_s.append(s[i])
        return ''.join(new_s)


if __name__ == '__main__':
    test = Solution()
    print(test.replaceSpace('we are superman'))
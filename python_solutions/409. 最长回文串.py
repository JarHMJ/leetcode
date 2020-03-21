import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        count = 0
        for v in counter.values():
            count += v % 2
        length = len(s)
        return length - count + 1 if count else length


a = Solution()
a.longestPalindrome('asdsfadsa')

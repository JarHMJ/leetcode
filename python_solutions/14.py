class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''

        return prefix


# TODO 有优化算法


if __name__ == '__main__':
    test = Solution()
    print(test.longestCommonPrefix(["dog", "racecar", "car"]))

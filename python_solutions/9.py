class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_reverse = str(x)[::-1]
        if x == int(x_reverse):
            return True
        else:
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome(10))

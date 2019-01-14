class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        s_list = list(s)
        length = len(s_list)
        num = 0
        while length:
            letter = s_list.pop(0)
            length -= 1
            if letter == 'I':
                if length and s_list[0] in ['V', 'X']:
                    letter_next = s_list.pop(0)
                    length -= 1
                    num += hash_map[letter_next] - hash_map[letter]
                else:
                    num += hash_map[letter]
            elif letter == 'V':
                num += hash_map[letter]
            elif letter == 'X':
                if length and s_list[0] in ['L', 'C']:
                    letter_next = s_list.pop(0)
                    length -= 1
                    num += hash_map[letter_next] - hash_map[letter]
                else:
                    num += hash_map[letter]
            elif letter == 'L':
                num += hash_map[letter]
            elif letter == 'C':
                if length and s_list[0] in ['D', 'M']:
                    letter_next = s_list.pop(0)
                    length -= 1
                    num += hash_map[letter_next] - hash_map[letter]
                else:
                    num += hash_map[letter]
            elif letter == 'D':
                num += hash_map[letter]
            elif letter == 'M':
                num += hash_map[letter]
        return num


if __name__ == '__main__':
    test = Solution()
    print(test.romanToInt('MCMXCIV'))

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex <= 33:
            result = [1] * (rowIndex + 1)
            for i in range(2, rowIndex + 1):
                for j in range(i - 1, 0, -1):
                    result[j] += result[j-1]
            return result


if __name__ == '__main__':
    test = Solution()
    print(test.getRow(5))

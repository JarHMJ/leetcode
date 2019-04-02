from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            if i > 1:
                # for j in range(1, i):
                #     tmp[j] = pre[j - 1] + pre[j]
                tmp = [1] + [sum(i) for i in zip(pre[:-1], pre[1:])] + [1]
            result.append(tmp)
            pre = tmp
        return result

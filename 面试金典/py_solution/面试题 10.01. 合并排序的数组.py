from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        l = m + n - 1
        while m and n:
            if A[m - 1] <= B[n - 1]:
                A[l] = B[n - 1]
                n -= 1
            else:
                A[l] = A[m - 1]
                m -= 1
            l -= 1
        while n:
            A[l] = B[n - 1]
            n -= 1
            l -= 1

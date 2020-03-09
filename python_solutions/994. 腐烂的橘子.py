from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        queue = deque()
        counter = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j, 0))
                elif val == 1:
                    counter += 1

        def neighbores(i, j):
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < r and 0 <= nj < c:
                    yield ni, nj

        minute = 0
        while queue:
            i, j, minute = queue.popleft()
            for ni, nj in neighbores(i, j):
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, minute + 1))
                    counter -= 1

        if counter == 0:
            return minute
        else:
            return -1

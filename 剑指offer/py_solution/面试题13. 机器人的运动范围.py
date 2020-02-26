class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        matrix = [[0] * n for i in range(m)]
        self.m = m
        self.n = n
        self.k = k
        self.count = 0
        self.dfs(matrix, 0, 0)
        return self.count

    def dfs(self, matrix, i, j):
        if not 0 <= i < self.m or not 0 <= j < self.n:
            return False
        if matrix[i][j] == 1:
            return False
        if i // 10 + i % 10 + j // 10 + j % 10 > self.k:
            return False
        matrix[i][j] = 1
        self.count += 1
        return (self.dfs(matrix, i - 1, j) or
                self.dfs(matrix, i + 1, j) or
                self.dfs(matrix, i, j - 1) or
                self.dfs(matrix, i, j + 1))

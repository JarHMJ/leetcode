from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.x = len(board)
        self.y = len(board[0])
        for i in range(self.x):
            for j in range(self.y):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        if i < 0 or i >= self.x or j < 0 or j >= self.y:
            return False
        if board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True
        board[i][j], tmp = '', word[0]
        target_word = word[1:]
        res = (self.dfs(board, target_word, i - 1, j) or
               self.dfs(board, target_word, i + 1, j) or
               self.dfs(board, target_word, i, j - 1) or
               self.dfs(board, target_word, i, j + 1))
        board[i][j] = tmp
        return res

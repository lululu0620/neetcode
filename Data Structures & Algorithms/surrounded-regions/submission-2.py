class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        def dfs(board, i, j):
            if i < 0 or i >= row or j < 0 or j >= col or visited[i][j] or board[i][j] == "X":
                return
            visited[i][j] = True
            dfs(board, i + 1, j)
            dfs(board, i - 1, j)
            dfs(board, i, j + 1)
            dfs(board, i, j - 1)
        for i in [0, row - 1]:
            for j in range(col):
                if board[i][j] == "O" and not visited[i][j]:
                    dfs(board, i, j)
        for i in range(row):
            for j in [0, col - 1]:
                if board[i][j] == "O" and not visited[i][j]:
                    dfs(board, i, j)
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == "O" and not visited[i][j]:
                    board[i][j] = "X"
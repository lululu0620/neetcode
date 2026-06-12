class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        minute = 0
        while queue:
            infected = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        count -= 1
                        if count == 0:
                            return minute + 1
            minute += 1
        return minute if count == 0 else -1
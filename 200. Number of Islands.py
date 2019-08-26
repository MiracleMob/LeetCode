class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            row = len(grid)
            col = len(grid[0])
            # 将1相连的区域变为0
            grid[r][c] = 0
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                dfs(grid, r - 1, c)
            if r + 1 < row and grid[r + 1][c] == '1':
                dfs(grid, r + 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                dfs(grid, r, c - 1)
            if c + 1 < col and grid[r][c + 1] == '1':
                dfs(grid, r, c + 1)

        row = len(grid)
        if row <= 0:
            return 0
        col = len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans


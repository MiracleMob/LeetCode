class Solution(object):
    # 递归遍历超出时间限制
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.path(grid, 0, 0)

    def path(self, grid, i, j):
        if i == len(grid) or j == len(grid[0]):
            return 1000000
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]

        return grid[i][j] + min(self.path(grid, i + 1, j),
                                self.path(grid, i, j + 1))


class Solution(object):
    # 递归遍历超出时间限制
    # 动态规划 dp[i][j] = (i,j) 到右下角的最短距离
    # dp[i][j] = grid[i][j] + min(dp[i][j+1], dp[j][i+1])
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] += grid[i][j + 1]
                elif i != len(grid) - 1 and j == len(grid[0]) - 1:
                    grid[i][j] += grid[i + 1][j]
                elif i < len(grid) - 1 and j < len(grid[0]) - 1:
                    grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])

        return grid[0][0]





class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = grid[i][j] + (grid[i-1][j] if i-1 >= 0 else 0) + (grid[i][j-1] if j-1 >= 0 else 0) - (grid[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0)
                if grid[i][j] <= k:
                    res += 1
                else:
                    break
        return res
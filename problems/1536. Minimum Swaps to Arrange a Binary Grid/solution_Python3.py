class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        found = [False for _ in range(grid_len)]
        steps = 0
        found_rows = 0
        for i in range(grid_len):
            for j in range(1, grid_len+1):
                not_found = False
                if grid[i][-j] != 0:
                    row = grid_len-j
                    while row < grid_len:
                        if not found[row]:
                            found[row] = True
                            steps += abs(row - i) + found[min(row,i):max(row,i)].count(True)
                                    found_rows += 1
                            not_found = True
                            break
                        row += 1
                if not_found:
                    break
        return steps
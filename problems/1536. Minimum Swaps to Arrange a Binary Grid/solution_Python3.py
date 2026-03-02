class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        swapped = [None for _ in range(grid_len)]
        for r, row in enumerate(grid):
            depth = grid_len
            for i in range(1, grid_len+1):
                if row[-i] != 0:
                    depth = i
                    break
            depth = grid_len - depth
            while depth < grid_len:
                if swapped[depth] is None:
                    swapped[depth] = r
                    break
                depth += 1
                if depth >= grid_len:
                    return -1
        steps = 0
        order = [n for n in range(grid_len)]
        for i in range(len(swapped)):
            current_index = order.index(swapped[i])
            current = order.pop(current_index)
            steps += current_index - i
            order.insert(i, current)
        return steps
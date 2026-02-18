class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        width = max(query_glass, query_row) + 1
        glasses = [[() for _ in range(width)] for _ in range(width)]
        def champagne(row, glass):
            if row == 0:
                status = (min(poured, 1.00000), max(0.00000, (poured - 1)/2))
                glasses[row][glass] = status
                return status
            left = 0
            if glass != 0:
                if glasses[row-1][glass-1]:
                    left = glasses[row-1][glass-1][1]
                else:
                    left = champagne(row-1, glass-1)[1]
            right = 0
            if glass <= row - 1:
                if glasses[row-1][glass]:
                    right = glasses[row-1][glass][1]
                else:
                    right = champagne(row-1, glass)[1]
            status = (min(left + right, 1.00000), max(0.00000, (left + right - 1)/2))
            glasses[row][glass] = status
            return status
        return champagne(query_row, query_glass)[0]
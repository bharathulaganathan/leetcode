class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        side = 1
        max_side = 0
        i = 0
        j = 0
        i_len = len(mat)
        j_len = len(mat[i])
        while i + side <= i_len and j + side <= j_len:
            sum = 0
            for k in range(i, i + side):
                for l in range(j, j + side):
                    sum += mat[k][l]
            if sum <= threshold:
                max_side = side
                side += 1
                continue
            if j + side >= j_len:
                j = 0
                i += 1
            else:
                j += 1
        return max_side
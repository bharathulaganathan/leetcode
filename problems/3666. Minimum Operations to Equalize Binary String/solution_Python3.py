from collections import deque
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        s_len = len(s)
        res = -1
        zeros = s.count("0")
        if k%2 == 0 and zeros%2 != 0:
            return -1
        if zeros == 0:
            return 0
        tracks = deque()
        visited = set()
        tracks.append((zeros, 0))
        visited.add(zeros)
        while tracks:
            current = tracks.popleft()
            zeros, steps = current
            for i in range(max(1,k-(s_len-zeros)),min(k,zeros)+1):
                new_zeros = zeros + k - 2*i
                if new_zeros == 0:
                    return steps + 1
                if new_zeros not in visited:
                    tracks.append((new_zeros, steps + 1))
                    visited.add(new_zeros)
        return res
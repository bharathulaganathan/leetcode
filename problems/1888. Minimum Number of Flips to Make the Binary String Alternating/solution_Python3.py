class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        i = 0
        c = 0
        for j in range(n):
            if j % 2 != int(s[j]):
                c += 1
        res = min(c, n - c)
        if n % 2 == 0:
            return res
        i = 0
        while i < n:
            if i % 2 != int(s[i]):
                c -= 1
                res = min(res, c, n-c)
            else:
                c += 1
                res = min(res, c, n-c)
            i += 1
        return res
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        p_count = 0
        n_count = 0
        current = s[0]
        for i in range(len(s)):
            if s[i] != current:
                ans += min(p_count, n_count)
                current = s[i]
                p_count = n_count
                n_count = 0
            n_count += 1
        return ans + min(p_count, n_count)
        
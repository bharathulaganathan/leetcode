class Solution:
    def minimumDeletions(self, s: str) -> int:
        len_s = len(s)
        rem = [0]*len_s
        b_left = 0
        for i in range(1, len_s):
            if s[i-1] == "b":
                b_left += 1
            rem[i] = b_left
        a_right = 0
        min_rem = rem[-1]
        for j in range(len_s - 2, -1, -1):
            if s[j+1] == "a":
                a_right += 1
            rem[j] += a_right
            min_rem = min(min_rem, rem[j])
        return min_rem



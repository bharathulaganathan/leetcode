class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans_len = max(len(a), len(b))
        ans = ""
        carry = 0
        i = 1
        while i < ans_len + 1 or carry:
            val = carry + (int(a[-i]) if i <= len(a) else 0) + (int(b[-i]) if i <= len(b) else 0)
            ans = str(val%2) + ans
            carry = int(val/2)
            i += 1
        return ans

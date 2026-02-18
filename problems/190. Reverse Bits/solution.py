class Solution:
    def reverseBits(self, n: int) -> int:
        BITS = 32
        ans = 0
        for i in range(BITS):
            rem = n % 2**(i+1)
            if rem != 0:
                ans += 2**(BITS-(i+1))
            n -= rem
        return ans

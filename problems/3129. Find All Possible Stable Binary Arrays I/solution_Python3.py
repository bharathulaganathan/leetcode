class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = (10**9) + 7
        memo = {}
        def get_stables(z, o, current):
            if (z, o, current) in memo:
                return memo[(z, o, current)]
            if z == 0 and o == 0:
                return 1
            res = 0
            for n in range(1, min(limit,z if current == 0 else o)+1):
                res += get_stables(z-n if current == 0 else z, o-n if current == 1 else o, (current+1)%2)
            memo[(z, o, current)] = res
            return res % mod
        return (get_stables(zero, one, 0) + get_stables(zero, one, 1)) % mod
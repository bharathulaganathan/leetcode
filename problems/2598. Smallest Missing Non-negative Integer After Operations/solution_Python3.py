class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        check = [False for _ in range(n)]
        done = dict()
        for i in range(n):
            rem = nums[i] % value
            if rem >= n:
                continue
            lowest = done.get(rem)
            if lowest == None:
                current = rem
            else:
                current = lowest
                if current + value < n:
                    current += value
            check[current] = True
            done[rem] = current
        for i in range(n):
            if check[i] == False:
                return i
        return n
        
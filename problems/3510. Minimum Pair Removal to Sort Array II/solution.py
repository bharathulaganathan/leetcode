class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        dec = 0
        pair_arr = []
        for k in range(len(nums)-1):
            n = k + 2
            if n >= len(nums):
                n = -1
            pair_arr.append(self.Pair(nums[k] + nums[k+1], k-1, k, k+1, n))
            if nums[k] > nums[k+1]:
                dec += 1
        merged = [0] * len(nums)
        opts = 0
        while dec > 0:
            min_sum = float('inf')
            min_index = len(pair_arr)
            pop_index = len(pair_arr)
            k = 0
            while k < len(pair_arr):
                if merged[pair_arr[k].i] == 0 and pair_arr[k].sum == nums[pair_arr[k].i] + nums[pair_arr[k].j]:
                    if pair_arr[k].sum < min_sum:
                        min_sum = pair_arr[k].sum
                        min_index = pair_arr[k].i
                        pop_index = k
                    elif pair_arr[k].sum == min_sum and pair_arr[k].i < min_index:
                        min_index = pair_arr[k].i
                        pop_index = k
                    k += 1
                else:
                    pair_arr.pop(k)
            pair = pair_arr.pop(pop_index)
            merged[pair.j] = 1
            if pair.p == None or merged[pair.p] == 1:
                for p in range(pair.i - 1, -1, -1):
                    if merged[p] == 0:
                        pair.p = p
                        break
                if pair.p == None or merged[pair.p] == 1:
                    pair.p = -1
            if pair.n == None or merged[pair.n] == 1:
                for n in range(pair.j+1, len(merged)):
                    if merged[n] == 0:
                        pair.n = n
                        break
                if pair.n == None or merged[pair.n] == 1:
                    pair.n = -1
            if nums[pair.p] > nums[pair.i] and pair.p >= 0:
                dec -= 1
            if nums[pair.i] > nums[pair.j]:
                dec -= 1
            if nums[pair.j] > nums[pair.n] and pair.n >= 0:
                dec -= 1
            nums[pair.i] = pair.sum
            if nums[pair.p] > pair.sum and pair.p >= 0:
                dec += 1
            if pair.sum > nums[pair.n] and pair.n >= 0:
                dec += 1
            if pair.p >= 0:
                pair_arr.append(self.Pair(pair.sum + nums[pair.p], None, pair.p, pair.i, pair.n))
            if pair.n >= 0:
                pair_arr.append(self.Pair(pair.sum + nums[pair.n], pair.p, pair.i, pair.n, None))
            opts += 1
        return opts
    class Pair:
        def __init__(self, sum, p, i, j, n):
            self.sum = sum
            self.p = p
            self.i = i
            self.j = j
            self.n = n
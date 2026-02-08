class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        opts = 0
        while True:
            min_index = 0
            if len(nums) <= 1:
                break
            min_sum = nums[0] + nums[1]
            dec = False
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    dec = True
                sum = nums[i] + nums[i + 1]
                if sum < min_sum:
                    min_sum = sum
                    min_index = i
            if not dec:
                break
            del nums[min_index + 1]
            nums[min_index] = min_sum
            opts += 1
        return opts
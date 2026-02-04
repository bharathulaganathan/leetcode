class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        i = 0
        while i < len(nums) - 3:
            if nums[i+1] > nums[i]:
                sum, next_trionic = self.singleTrionic(nums, i)
                max_sum = max(sum, max_sum)
                i = next_trionic
            else:
                i += 1
        return max_sum
    def singleTrionic(self, nums, i):
        trionic = 1
        strict = False
        sum = nums[i]
        max_sum = float('-inf')
        last_dec = i
        while i < len(nums):
            if i == len(nums) - 1 and trionic != 3:
                return (float('-inf'), last_dec)
            if trionic == 1:
                if nums[i+1] > nums[i]:
                    sum += nums[i+1]
                    sum = max(sum, nums[i] + nums[i+1])
                    i += 1
                    last_dec = i
                else:
                    trionic = 2
            elif trionic == 2:
                if nums[i+1] < nums[i]:
                    strict = True
                    sum += nums[i+1]
                    i += 1
                    last_dec = i
                else:
                    if not strict:
                        return (float('-inf'), last_dec)
                    else:
                        trionic += 1
                        strict = False
            else:
                if i == len(nums) - 1:
                    return (max_sum, last_dec)
                if nums[i+1] > nums[i]:
                    strict = True
                    sum += nums[i+1]
                    max_sum = max(sum, max_sum)
                    i += 1
                else:
                    if not strict:
                        return (float('-inf'), last_dec)
                    else:
                        return (max_sum, last_dec)



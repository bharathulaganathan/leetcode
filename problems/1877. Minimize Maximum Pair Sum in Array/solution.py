class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_max = 0
        for i in range(int(len(nums)/2)):
            sum = nums[i] + nums[-(i+1)]
            if sum > min_max:
                min_max = sum
        return min_max
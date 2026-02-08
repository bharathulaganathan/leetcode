class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        min_diff = nums[0] - nums[-1]
        for i in range(len(nums)-k+1):
            diff = nums[i] - nums[i+k-1]
            if diff < min_diff:
                min_diff = diff
        return min_diff
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        for n in range(len(nums)):
            result.append(nums[(n+nums[n])%length])
        return result
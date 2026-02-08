class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            and_ = -1
            for j in range(num):
                if j | j + 1 == num:
                    and_ = j
                    break
            ans.append(and_)
        return ans
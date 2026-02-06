class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        rem = 0
        min = 0
        max = len(nums) - 1
        while True:
            if nums[max - rem] <= nums[min] * k or nums[max] <= nums[min + rem] * k:
                max_rem = rem
                while True:
                    rem -= 1
                    min = 0
                    max = len(nums) - 1 - rem
                    found = False
                    while max < len(nums):
                        if nums[max] <= nums[min] * k:
                            found = True
                            break
                        min += 1
                        max += 1
                    if not found:
                        return rem + 1
                return max_rem
            rem += 1


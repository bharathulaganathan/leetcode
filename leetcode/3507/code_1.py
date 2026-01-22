from typing import List


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


testcases = [[5, 2, 3, 1], [1, 2, 2]]

expected = [2, 0]

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minimumPairRemoval(case)
    exp = expected[c]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")

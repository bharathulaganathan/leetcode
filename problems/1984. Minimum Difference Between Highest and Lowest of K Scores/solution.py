from typing import List
import os
import json

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        min_diff = nums[0] - nums[-1]
        for i in range(len(nums)-k+1):
            diff = nums[i] - nums[i+k-1]
            if diff < min_diff:
                min_diff = diff
        return min_diff

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "testcases.json")) as file:
    testcases = json.load(file)

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minimumDifference(case["input"]["nums"], case["input"]["k"])
    exp = case["output"]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")


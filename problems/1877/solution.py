from typing import List
import os
import json

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_max = 0
        for i in range(int(len(nums)/2)):
            sum = nums[i] + nums[-(i+1)]
            if sum > min_max:
                min_max = sum
        return min_max


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "testcases.json")) as file:
    testcases = json.load(file)

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minPairSum(case["input"])
    exp = case["output"]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")


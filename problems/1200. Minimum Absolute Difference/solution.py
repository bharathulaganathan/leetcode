from typing import List
import os
import json

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        ans = [[arr[0], arr[1]]]
        for i in range(1, len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                ans.append([arr[i], arr[i+1]])
        return ans


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "testcases.json")) as file:
    testcases = json.load(file)

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minimumAbsDifference(case["input"])
    exp = case["output"]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")


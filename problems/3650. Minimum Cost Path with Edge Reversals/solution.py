from typing import List
import os
import json

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "testcases.json")) as file:
    testcases = json.load(file)

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minCost(case["input"]["n"], case["input"]["edges"])
    exp = case["output"]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")


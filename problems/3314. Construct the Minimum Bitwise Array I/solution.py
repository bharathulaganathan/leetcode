from typing import List


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


testcases = [[2, 3, 5, 7], [11, 13, 31]]

expected = [[-1, 1, 4, 3], [9, 12, 15]]

solution = Solution()
failed = False
for c, case in enumerate(testcases):
    sol = solution.minBitwiseArray(case)
    exp = expected[c]
    if sol != exp:
        failed = True
        print(f"Case {c + 1} failed!")
        print(f"Expected {exp} but got {sol}")
if not failed:
    print(f"All {len(testcases)} testcases passed!")

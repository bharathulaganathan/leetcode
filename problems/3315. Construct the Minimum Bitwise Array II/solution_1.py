from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            bit_num = bin(num)[2:]
            ans_ = -1
            if bit_num[-1] == "0":
                ans.append(ans_)
                continue
            num_1s = 0
            ans_0 = bit_num
            for i in range(len(bit_num) - 1):
                index = len(bit_num) - i - 1
                if bit_num[index] == "1":
                    num_1s += 1
                    ans_0 = ans_0[:index] + "0" + ans_0[index + 1 :]
                else:
                    break
            ansp1 = ans_0
            for k in range(num_1s + 1):
                ans_ = int(ansp1, 2) - 1
                if ans_ | int(ansp1, 2) == num:
                    ans.append(ans_)
                    break
                index = len(bit_num) - k - 1
                ansp1 = ans_0
                ansp1 = ansp1[:index] + "1" + ansp1[index + 1 :]
        return ans


testcases = [
    [2, 3, 5, 7],
    [11, 13, 31],
    [
        884532611,
        741533369,
        868936609,
        816315823,
        150570781,
        346594697,
        334726181,
        921762641,
        89355881,
        403165729,
        931242733,
    ],
]

expected = [
    [-1, 1, 4, 3],
    [9, 12, 15],
    [
        884532609,
        741533368,
        868936608,
        816315815,
        150570780,
        346594696,
        334726180,
        921762640,
        89355880,
        403165728,
        931242732,
    ],
]

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

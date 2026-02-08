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
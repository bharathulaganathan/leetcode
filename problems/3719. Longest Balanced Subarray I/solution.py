class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        nums_len = len(nums)
        counter = nums_len
        diff = nums_len - counter
        odd = {}
        even = {}

        def add_num(num):
            if num == 0:
                pass
            elif num % 2 == 1:
                odd[num] = odd.get(num, 0) + 1
            else:
                even[num] = even.get(num, 0) + 1

        def remove_num(num):
            if num == 0:
                pass
            elif num % 2 == 1:
                odd[num] -= 1
                if odd[num] == 0:
                    del odd[num]
            else:
                even[num] -= 1
                if even[num] == 0:
                    del even[num]

        def is_balanced():
            if len(odd) == len(even):
                return True
            return False

        for num in nums:
            add_num(num)
        if is_balanced():
            return counter
        counter -= 1
        while counter > 1:
            diff += 1
            remove_num(nums[-diff])
            if is_balanced():
                return counter
            for i in range(0, diff):
                remove_num(nums[i])
                add_num(nums[i+counter])
                if is_balanced():
                    return counter
            counter -= 1
            if not counter:
                return counter
            diff += 1
            remove_num(nums[diff-1])
            if is_balanced():
                return counter
            for i in range(1, diff+1):
                remove_num(nums[-i])
                add_num(nums[-(i+counter)])
                if is_balanced():
                    return counter
            counter -= 1
        return 0



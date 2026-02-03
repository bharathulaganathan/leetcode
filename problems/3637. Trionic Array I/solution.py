class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        trionic = 0
        strict = False
        i = 0
        while i < len(nums) - 1:
            if trionic % 2 == 0:
                if nums[i+1] > nums[i]:
                    strict = True
                    i += 1
                else:
                    if strict == False:
                        return False
                    trionic += 1
                    strict = False
            else:
                if nums[i+1] < nums[i]:
                    strict = True
                    i += 1
                else:
                    if strict == False:
                        return False
                    trionic += 1
                    strict = False
        if trionic == 2 and strict:
            return True
        else:
            return False

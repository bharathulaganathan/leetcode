class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bin_len = len(nums[0])
        nums = set(nums)
        def get_bins(current):
            for b in ["0", "1"]:
                new_current = current + b
                if len(new_current) == bin_len:
                    if new_current not in nums:
                        return new_current
                elif len(new_current) < bin_len:
                    new_bin = get_bins(new_current)
                    if new_bin:
                        return new_bin
        return get_bins("")

        
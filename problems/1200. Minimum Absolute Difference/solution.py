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
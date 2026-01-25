from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            x_diff = abs(points[i][0] - points[i + 1][0])
            y_diff = abs(points[i][1] - points[i + 1][1])
            time += max(x_diff, y_diff)
        return time


test_cases = [
    [[1, 1], [3, 4], [-1, 0]],
    [[3, 2], [-2, 2]]
    ]

solution = Solution()
for p in range(len(test_cases)):
    print(f"Case {p + 1}: {solution.minTimeToVisitAllPoints(test_cases[p])}")

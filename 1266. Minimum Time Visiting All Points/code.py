from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        current = points.pop(0)
        for point in points:
            while True:
                if current == point:
                    break
                if current[0] < point [0]:
                    current[0] += 1
                elif current[0] > point [0]:
                    current[0] -= 1
                if current[1] < point [1]:
                    current[1] += 1
                elif current[1] > point [1]:
                    current[1] -= 1
                time += 1
        return time
    
points = [[1,1],[3,4],[-1,0]]

sol = Solution()
print(sol.minTimeToVisitAllPoints(points))

from typing import List
import os
import json
import heapq

import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for _ in range(n)]
        for u, v, w in edges:
            nodes[u].append((v, w))
            nodes[v].append((u, w * 2))
        heap = [(0, 0)]
        dist = [float('inf')] * n
        dist[0] = 0
        while heap:
            cost, node = heapq.heappop(heap)
            if cost > dist[node]:
                continue
            if node == n - 1:
                return cost
            for nxt, w in nodes[node]:
                new_cost = cost + w
                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(heap, (new_cost, nxt))
        return -1

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


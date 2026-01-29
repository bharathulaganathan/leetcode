from typing import List
import os
import json
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        nodes = [set() for _ in range(n)]
        for e in range(len(edges)):
            nodes[edges[e][0]].add((edges[e][2], edges[e][1]))
            nodes[edges[e][1]].add((edges[e][2]*2, edges[e][0]))
        heap = [(0, 0)]
        heapq.heapify(heap)
        done = set()
        max_w = [float('inf')]*n
        max_w[0] = 0
        while len(heap) > 0:
            w, node = heapq.heappop(heap)
            if node == n - 1:
                return w
            done.add(node)
            for next in nodes[node]:
                if next[1] not in done:
                    next_node = next[1]
                    next_w = min(next[0] + w, max_w[next_node])
                    max_w[next_node] = next_w
                    heapq.heappush(heap, (next_w, next_node))
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


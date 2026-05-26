from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)
        pyramid = list()
        for i in range(1, n):
            pyramid.append([None for _ in range(i)])
        pyramid.append([c for c in bottom])
        self.blocks = defaultdict(list)
        for l, r, t in allowed:
            self.blocks[(l, r)].append(t)

        def add_block(i, j, pyramid):
            if j == len(pyramid[i]) - 1:
                i = -1
                j = 0
            if i == 0:
                return True
            state = False
            cur = (pyramid[i][j], pyramid[i][j + 1])
            for block in self.blocks[cur]:
                new_pyramid = pyramid.copy()
                new_pyramid[i - 1][j] = block
                state = state or add_block(i, j + 1, new_pyramid)
            return state

        return add_block(n - 1, 0, pyramid)

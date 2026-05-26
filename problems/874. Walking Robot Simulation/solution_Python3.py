class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = y = 0
        d = "U"
        anti = {"U": "L", "L": "D", "D": "R", "R": "U"}
        clock = {"U": "R", "R": "D", "D": "L", "L": "U"}
        obstacles = map(tuple, obstacles)
        obstacles = set(obstacles)
        res = 0
        for c in commands:
            if c < 0:
                if c == -1:
                    d = clock[d]
                elif c == -2:
                    d = anti[d]
            else:
                if d == "U":
                    for i in range(y+1,y+c+1):
                        if (x,i) in obstacles:
                            y = i - 1
                            break
                    else:
                        y = y + c
                elif d == "D":
                    for i in range(y-1,y-c-1,-1):
                        if (x,i) in obstacles:
                            y = i + 1
                            break
                    else:
                        y = y - c
                elif d == "R":
                    for i in range(x+1,x+c+1):
                        if (i,y) in obstacles:
                            x = i - 1
                            break
                    else:
                        x = x + c
                elif d == "L":
                    for i in range(x-1,x-c-1,-1):
                        if (i,y) in obstacles:
                            x = i + 1
                            break
                    else:
                        x = x - c
                res = max(res, (x**2) + (y**2))
        return res
        
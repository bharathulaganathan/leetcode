import heapq
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        stop = list()
        if coins[0][0] < 0:
            stop.append(coins[0][0])
        total = 0 if coins[0][0] < 0 else coins[0][0]
        heapq.heapify_max(stop)
        coins[0][0] = {"total": total, "stop": stop}
        for i in range(len(coins)-1):
            total = coins[i][0]["total"]
            stop = coins[i][0]["stop"].copy()
            if coins[i+1][0] < 0:
                if len(stop) < 2:
                    heapq.heappush_max(stop, coins[i+1][0])
                else:
                    large = heapq.heappushpop_max(stop, coins[i+1][0])
                    total += large
            else:
                total += coins[i+1][0]
            coins[i+1][0] = {"total": total, "stop": stop}
        for j in range(len(coins[0])-1):
            total = coins[0][j]["total"]
            stop = coins[0][j]["stop"].copy()
            if coins[0][j+1] < 0:
                if len(stop) < 2:
                    heapq.heappush_max(stop, coins[0][j+1])
                else:
                    large = heapq.heappushpop_max(stop, coins[0][j+1])
                    total += large
            else:
                total += coins[0][j+1]
            coins[0][j+1] = {"total": total, "stop": stop}
        for i in range(len(coins)-1):
            for j in range(len(coins[i])-1):
                total_top = coins[i][j+1]["total"]
                total_bot = coins[i+1][j]["total"]
                stop_top = coins[i][j+1]["stop"].copy()
                stop_bot = coins[i+1][j]["stop"].copy()
                if coins[i+1][j+1] < 0:
                    if len(stop_top) < 2:
                        heapq.heappush_max(stop_top, coins[i+1][j+1])
                    else:
                        large_top = heapq.heappushpop_max(stop_top, coins[i+1][j+1])
                        total_top += large_top
                    if len(stop_bot) < 2:
                        heapq.heappush_max(stop_bot, coins[i+1][j+1])
                    else:
                        large_bot = heapq.heappushpop_max(stop_bot, coins[i+1][j+1])
                        total_bot += large_bot
                else:
                    total_top += coins[i+1][j+1]
                    total_bot += coins[i+1][j+1]
                if total_top > total_bot:
                    coins[i+1][j+1] = {"total": total_top, "stop": stop_top}
                elif total_bot > total_top:
                    coins[i+1][j+1] = {"total": total_bot, "stop": stop_bot}
                else:
                    if sum(stop_top) > sum(stop_bot):
                        coins[i+1][j+1] = {"total": total_top, "stop": stop_top}
                    else:
                        coins[i+1][j+1] = {"total": total_bot, "stop": stop_bot}
        return coins[-1][-1]["total"]
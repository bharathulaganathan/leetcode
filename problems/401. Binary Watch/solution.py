class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = ["h-1", "h-2", "h-4", "h-8", "m-1", "m-2", "m-4", "m-8", "m-16", "m-32"]
        ans = set()
        checked = set()

        def create_comb(done, remain, switch):
            if switch == turnedOn:
                get_time(done)
                return
            for r in range(len(remain)):
                new_remain = remain.copy()
                new_done = done.copy()
                new_done.append(new_remain.pop(r))
                check = tuple(new_done)
                if check not in checked:
                    checked.add(check)
                    create_comb(new_done, new_remain, switch+1)

        def get_time(done):
            time = {"h": 0, "m": 0}
            for t in done:
                hand, val = t.split("-")
                time[hand] += int(val)
            if time["h"] > 11 or time["m"] > 59:
                return
            ans.add(f"{time["h"]}:{time["m"]:02d}")

        if turnedOn > 8:
            return []
        create_comb([], times, 0)
        return list(ans)

import math
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        alf = {}
        for i in range(26):
            alf[chr(ord("A")+i)] = (i//6,i%6)
        total = 0
        for w in range(1,n):
            total += abs(alf[word[w-1]][0] - alf[word[w]][0]) + abs(alf[word[w-1]][1] - alf[word[w]][1])
        res = math.inf
        for i in range(n-1):
            l = total
            r = 0
            li = [x for x in range(i+1)]
            ri = list()
            for w in range(i+1,n):
                rem = abs(alf[word[li[-1]]][0] - alf[word[w]][0]) + abs(alf[word[li[-1]]][1] - alf[word[w]][1])
                com = 0
                if w + 1 < n:
                    rem += abs(alf[word[w]][0] - alf[word[w+1]][0]) + abs(alf[word[w]][1] - alf[word[w+1]][1])
                    com = abs(alf[word[li[-1]]][0] - alf[word[w+1]][0]) + abs(alf[word[li[-1]]][1] - alf[word[w+1]][1])
                new_l = l - rem + com
                new_r = r
                if ri:
                    new_r += abs(alf[word[ri[-1]]][0] - alf[word[w]][0]) + abs(alf[word[ri[-1]]][1] - alf[word[w]][1])
                if new_l + new_r <= l + r:
                    l = new_l
                    r = new_r
                    ri.append(w)
                else:
                    li.append(w)
            res = min(res, l+r)
        return res
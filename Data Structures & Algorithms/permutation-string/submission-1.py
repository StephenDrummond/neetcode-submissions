class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        t1 = Counter(s1)
        t2 = Counter()
        l, r = 0, len(s1) -1

        for i in range(len(s1)):
            t2[s2[i]] += 1

        while r < len(s2):
            if t1 == t2:
                return True
            print(t1, t2)
            t2[s2[l]] -= 1
            l += 1
            r += 1
            if r >= len(s2): break
            t2[s2[r]] += 1
            
        return False
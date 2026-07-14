class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[0:len(s1)])
        l, r = 0, len(s1) - 1

        if c1 == c2:
            return True

        while r < len(s2) - 1:
            r += 1
            c2[s2[r]] += 1
            c2[s2[l]] -= 1
            l += 1
            if c1 == c2:
                return True


        return False
            
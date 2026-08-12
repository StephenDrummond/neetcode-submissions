class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        st = set()
        for i in range(len(s)):
            if s[i] not in hm:
                if t[i] in st:
                    return False
                hm[s[i]] = t[i]
                st.add(t[i])
            else:
                if hm[s[i]] != t[i]:
                    return False
        print(hm)
        return True
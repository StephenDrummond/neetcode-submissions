class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in range(len(strs)):
            s = strs[i]
            afbt = [0] * 26

            for c in s:
                afbt[ord(c) - 97] += 1

            afbt = tuple(afbt)

            if afbt in seen:
                seen[afbt].append(s)
            else:
                seen[afbt] = [s]
        
        return list(seen.values())
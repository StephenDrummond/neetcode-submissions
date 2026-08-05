class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            age = d[11:13]
            if int(age) > 60:
                ans += 1
        return ans
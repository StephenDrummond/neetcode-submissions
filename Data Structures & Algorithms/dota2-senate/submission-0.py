class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r, d = R.popleft(), D.popleft()

            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        
        return 'Radiant' if R else 'Dire'
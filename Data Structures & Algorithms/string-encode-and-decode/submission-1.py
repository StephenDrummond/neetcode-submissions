class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            n = len(s)
            encoded += str(n) + 'ā' + s
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        start = 0
        end = 1
        m = len(s)
        print(s)

        while end < m:
            while s[end] != 'ā':
                end += 1
            n = int(s[start:end])
            word = s[end + 1: end + n + 1]
            decoded.append(word)
            end += n + len(str(n))
            start += n + len(str(n)) + 1

        return decoded
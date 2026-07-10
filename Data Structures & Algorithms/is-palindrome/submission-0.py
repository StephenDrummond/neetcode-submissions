class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub(r"[^a-zA-Z0-9]", "", s)
        l, r = 0, len(s) - 1

        while r >= l:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
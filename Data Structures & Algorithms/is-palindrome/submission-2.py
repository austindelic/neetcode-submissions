class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = -1
        s = "".join(c for c in s.lower() if c.isalnum())
        for _ in range(len(s) // 2):
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ""
        start = 0
        end = 1
        max_len = 0
        if end == len(s):
            return 1
        while end < len(s):
            sub = s[start:end + 1]
            if len(sub) != len(set(sub)):
                start += sub.index(sub[-1]) + 1
                sub = s[start:end + 1]
            if len(sub) > max_len:
                max_len = len(sub)

            end += 1
        return max_len
# [3] Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sp = ep = 0
        point = 0
        hash = {}
        while ep < len(s):
            if s[ep] in hash and hash[s[ep]] >= sp:
                sp = hash[s[ep]] + 1
            hash[s[ep]] = ep
            point = max(point, ep-sp+1)
            ep += 1
        return point
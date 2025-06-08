# [387] First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in hash:
            if hash[i] == 1:
                return s.find(i)
        return -1
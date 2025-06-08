# [392] Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0
        while tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        return len(s) == sp

# test
import pytest

def test_isSubsequence():
    solution = Solution()
    assert solution.isSubsequence("abc", "ahbgdc") is True
    assert solution.isSubsequence("axc", "ahbgdc") is False
    assert solution.isSubsequence("aaaaaa", "bbaaaa") is False
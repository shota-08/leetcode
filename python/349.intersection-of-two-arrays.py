# [349] Intersection of Two Arrays

from typing import List

# O(n*m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res

# O(n+m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        res = []
        for i in nums1:
            if i not in set1:
                set1.add(i)
        for i in nums2:
            if i in set1 and i not in set2:
                res.append(i)
            if i not in set2:
                set2.add(i)
        return res
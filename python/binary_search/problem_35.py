# [35] Search Insert Position

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left
from problem_35 import Solution

def test_searchInsert():
    solution = Solution()

    # case:1
    assert solution.searchInsert([1,3,5,6], 5) == 2

    # case:2
    assert solution.searchInsert([1,3,5,6], 2) == 1

    # case:3
    assert solution.searchInsert([1,3,5,6], 7) == 4

    # case:4
    assert solution.searchInsert([1,3], 2) == 1


from problem_33 import Solution

def test_search():
    solution = Solution()

    # case:1
    assert solution.search([4,5,6,7,0,1,2], 0) == 4

    # case:2
    assert solution.search([4,5,6,7,0,1,2], 3) == -1

    # case:3
    assert solution.search([1], 0) == -1

    # case:4
    assert solution.search([3,1], 1) == 1
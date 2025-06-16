from problem_112 import Solution
from utils.build_tree import build_tree_from_list


def test_hasPathSum():
    solution = Solution()

    # case1
    tree1 = build_tree_from_list([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert solution.hasPathSum(tree1, 22) is True

    # case2
    tree2 = build_tree_from_list([1,2,3])
    assert solution.hasPathSum(tree2, 5) is False

    # case3
    tree3 = build_tree_from_list([])
    assert solution.hasPathSum(tree3, 0) is False

    # case4
    tree4 = build_tree_from_list([1])
    assert solution.hasPathSum(tree4, 1) is True
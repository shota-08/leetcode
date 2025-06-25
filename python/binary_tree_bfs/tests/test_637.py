from problem_637 import Solution
from utils.build_tree import build_tree_from_list

def test_averageOfLevels():
    solution = Solution()

    # case:1
    tree1 = build_tree_from_list([3,9,20,None,None,15,7])
    assert solution.averageOfLevels(tree1) == [3.00000,14.50000,11.00000]

    # case:2
    tree2 = build_tree_from_list([3,9,20,15,7])
    assert solution.averageOfLevels(tree2) == [3.00000,14.50000,11.00000]
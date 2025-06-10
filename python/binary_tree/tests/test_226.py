from problem_226 import Solution
from utils.build_tree import build_tree_from_list, is_same_tree


def test_invertTree():
    solution = Solution()

    # case:1
    tree1 = build_tree_from_list([4,2,7,1,3,6,9])
    solution.invertTree(tree1)
    expected_tree1 = build_tree_from_list([4,7,2,9,6,3,1])
    assert is_same_tree(tree1, expected_tree1)

    # case:2
    tree2 = build_tree_from_list([2,1,3])
    solution.invertTree(tree2)
    expected_tree2 = build_tree_from_list([2,3,1])
    assert is_same_tree(tree2, expected_tree2)

    # case:3
    tree3 = build_tree_from_list([])
    solution.invertTree(tree3)
    expected_tree3 = build_tree_from_list([])
    assert is_same_tree(tree3, expected_tree3)
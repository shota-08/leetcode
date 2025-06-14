from problem_114 import Solution
from utils.build_tree import build_tree_from_list, is_same_tree

def test_flatten():
    solution = Solution()

    # case:1
    tree1 = build_tree_from_list([1,2,5,3,4,None,6])
    solution.flatten(tree1)
    expected_tree1 = build_tree_from_list([1,None,2,None,3,None,4,None,5,None,6])
    assert is_same_tree(tree1, expected_tree1)

    # case:2
    tree2 = build_tree_from_list([0])
    solution.flatten(tree2)
    expected_tree2 = build_tree_from_list([0])
    assert is_same_tree(tree2, expected_tree2)

    # case:3
    tree3 = build_tree_from_list([])
    solution.flatten(tree3)
    expected_tree3 = build_tree_from_list([])
    assert is_same_tree(tree3, expected_tree3)

    # case:4
    tree4 = build_tree_from_list([1,None,2,None,3])
    solution.flatten(tree4)
    expected_tree4 = build_tree_from_list([1,None,2,None,3])
    assert is_same_tree(tree4, expected_tree4)
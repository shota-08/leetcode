from problem_101 import Solution
from utils.build_tree import build_tree_from_list

def test_invertTree():
    solution = Solution()

    # case1:
    tree_list1 = [1,2,2,3,4,4,3]
    tree1 = build_tree_from_list(tree_list1)
    assert solution.invertTree(tree1) is True

    # case2:
    tree_list2 = [1,2,2,None,3,None,3]
    tree2 = build_tree_from_list(tree_list2)
    assert solution.invertTree(tree2) is False

    # case3:
    tree_list3 = [1]
    tree3 = build_tree_from_list(tree_list3)
    assert solution.invertTree(tree3) is True
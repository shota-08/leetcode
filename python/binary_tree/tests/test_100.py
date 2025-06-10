from problem_100 import Solution
from utils.build_tree import build_tree_from_list

def test_isSameTree():
    solution = Solution()

    # case:1
    list_p1 = [1,2,3]
    list_q1 = [1,2,3]
    tree_p1 = build_tree_from_list(list_p1)
    tree_q1 = build_tree_from_list(list_q1)
    assert solution.isSameTree(tree_p1, tree_q1) is True

    # case:2
    list_p2 = [1,2]
    list_q2 = [1,None,2]
    tree_p2 = build_tree_from_list(list_p2)
    tree_q2 = build_tree_from_list(list_q2)
    assert solution.isSameTree(tree_p2, tree_q2) is False

    # case:3
    list_p3 = [1,2,1]
    list_q3 = [1,1,2]
    tree_p3 = build_tree_from_list(list_p3)
    tree_q3 = build_tree_from_list(list_q3)
    assert solution.isSameTree(tree_p3, tree_q3) is False
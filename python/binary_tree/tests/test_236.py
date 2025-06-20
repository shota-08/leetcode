from problem_236 import Solution
from utils.build_tree import build_tree_from_list, find_node


def test_lowestCommonAncestor():
    solution = Solution()

    # case:1
    tree_list1 = [3,5,1,6,2,0,8,None,None,7,4]
    tree1 = build_tree_from_list(tree_list1)
    p1 = find_node(tree1, 5)
    q1 = find_node(tree1, 1)
    expected_lca1 = find_node(tree1, 3)
    assert solution.lowestCommonAncestor(tree1, p1, q1) is expected_lca1

    # case:2
    tree_list2 = [3,5,1,6,2,0,8,None,None,7,4]
    tree2 = build_tree_from_list(tree_list2)
    p2 = find_node(tree2, 5)
    q2 = find_node(tree2, 4)
    expected_lca2 = find_node(tree2, 5)
    assert solution.lowestCommonAncestor(tree2, p2, q2) is expected_lca2

    # case:3
    tree_list3, p3, q3 = [1,2], 1, 2
    tree3 = build_tree_from_list(tree_list3)
    p3 = find_node(tree3, 1)
    q3 = find_node(tree3, 2)
    expected_lca3 = find_node(tree3, 1)
    assert solution.lowestCommonAncestor(tree3, p3, q3) is expected_lca3

from problem_104 import Solution
from utils.build_tree import build_tree_from_list

def test_maxDepth():
    solution = Solution()

    # case:1
    tree_list1 = [3,9,20,None,None,15,7]
    tree1 = build_tree_from_list(tree_list1)
    assert solution.maxDepth(tree1) == 3

    # case:2
    tree_list2 = [1,None,2]
    tree2 = build_tree_from_list(tree_list2)
    assert solution.maxDepth(tree2) == 2

    # case:3
    tree_list3 = []
    tree3 = build_tree_from_list(tree_list3)
    assert solution.maxDepth(tree3) == 0
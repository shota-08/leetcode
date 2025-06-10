# [104] Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

# [114] Flatten Binary Tree to Linked List

class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        while root:
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                temp.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

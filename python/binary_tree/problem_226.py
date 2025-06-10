# [226] Invert Binary Tree

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
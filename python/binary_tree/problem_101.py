# [101] Symmetric Tree

class Solution:
    def invertTree(self, root):

        def is_mirror(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
            return is_mirror(root1.right, root2.left) and is_mirror(root1.left, root2.right)

        return is_mirror(root.right, root.left)
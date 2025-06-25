# [637] Average of Levels in Binary Tree

class Solution:
    def averageOfLevels(self, root):
        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            level_sum = 0
            for i in range(level_size):
                current_node = queue.pop(0)
                level_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            level_avg = level_sum / level_size
            result.append(level_avg)
        return result
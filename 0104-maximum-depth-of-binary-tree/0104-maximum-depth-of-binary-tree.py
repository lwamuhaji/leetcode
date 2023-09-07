# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [(root, 1)]
        while queue:
            current, depth = queue.pop(0)
            if current.left:
                queue.append((current.left, depth + 1))
            if current.right:
                queue.append((current.right, depth + 1))
        return depth
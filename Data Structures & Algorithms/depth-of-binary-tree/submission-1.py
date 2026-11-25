# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = {None: 0}                      # results of the finished "calls"
        stack = [(root, False)]
        while stack:
            node, children_done = stack.pop()
            if children_done:                  # both children are finished: combine
                depth[node] = 1 + max(depth[node.left], depth[node.right])
            else:
                stack.append((node, True))     # come back to this node after its children
                for child in (node.left, node.right):
                    if child:
                        stack.append((child, False))
        return depth[root]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def visit(node):    # (best downward path from node, best path anywhere in the subtree)
            if not node:
                return 0, float("-inf")
            left_gain, left_best = visit(node.left)
            right_gain, right_best = visit(node.right)
            left_gain = max(left_gain, 0)      # a negative branch is not worth taking
            right_gain = max(right_gain, 0)
            through_node = node.val + left_gain + right_gain       # path that bends at this node
            best = max(left_best, right_best, through_node)
            return node.val + max(left_gain, right_gain), best     # a parent can use only one side
            
        return visit(root)[1]
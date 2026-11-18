# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result, stack = [], []
        node = root
        while node or stack:
            while node:                        # go left as far as possible
                stack.append(node)
                node = node.left
            node = stack.pop()                 # leftmost node not visited yet
            result.append(node.val)
            node = node.right                  # then its right subtree
        return result
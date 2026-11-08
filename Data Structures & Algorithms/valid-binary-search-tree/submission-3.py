# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValidSubBST(root: Optional[TreeNode], crtMin : int, crtMax : int) :
            if not root : 
                return True
            if crtMin < root.val < crtMax : 
                leftIsBst = isValidSubBST(root.left, crtMin, root.val)
                rightIsBst = isValidSubBST(root.right, root.val, crtMax)
                return leftIsBst and rightIsBst
            return False
            
        return isValidSubBST(root, float("-inf"), float("inf"))
            

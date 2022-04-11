########## Prob Link : https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root == None:
                return (True, 0)
            leftB, leftH = helper(root.left)
            rightB, rightH = helper(root.right)
            return(rightB and leftB and abs(leftH - rightH) <= 1, max(leftH, rightH)+1)
        return helper(root)[0]
 
            

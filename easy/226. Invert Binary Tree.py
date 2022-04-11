### Prob Link : https://leetcode.com/problems/invert-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if root == None:
                return root
            left = helper(root.left)
            right = helper(root.right)
            root.left = right
            root.right = left
            return root
        return(helper(root))

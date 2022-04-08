###### prob link : https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None and subRoot.left is None and subRoot.right is None:
            return root.val == subRoot.val
        def preorder(node):
            if node is None :
                return('*')
            return(str(node.val) + preorder(node.left) + preorder(node.right))
        return preorder(subRoot) in preorder(root)

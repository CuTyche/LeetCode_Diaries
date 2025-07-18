# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

 # No typing
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight 
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    def maxHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, sum, isLeaf, targetSum):
        if root == None:
            if sum == targetSum and isLeaf:
                return True
            else:
                return False
        else:
            return self.solve(root.left, sum+root.val, root.left == None and root.right == None, targetSum) or self.solve(root.right, sum+root.val, root.left == None and root.right == None, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        else:
            return self.solve(root, 0, root.left == None and root.right == None, targetSum)

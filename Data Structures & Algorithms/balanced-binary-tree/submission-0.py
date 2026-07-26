# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        b=[True]
        def dfs(curr):
            if not curr:
                return 0
            else:
                left=dfs(curr.left)
                right=dfs(curr.right)
                if abs(left-right)>=2:
                    b[0]=False
                    return 0
                return (1+max(left,right))
        dfs(root)
        return b[0]
        
        
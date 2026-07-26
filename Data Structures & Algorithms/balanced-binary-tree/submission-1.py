# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.b=1
        def dfs(curr):
            if not curr:
                return 0
            else:
                left=dfs(curr.left)
                right=dfs(curr.right)
                if abs(left-right)>1:
                    self.b=0
                    return 0
                return(1+max(left,right))
        dfs(root)
        if self.b==1:
            return True
        else:
            return False

        
        
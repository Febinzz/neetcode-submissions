# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def norder(node):
            if not node:
                return
            norder(node.left)
            res.append(node.val)
            norder(node.right)
        norder(root)
        return res
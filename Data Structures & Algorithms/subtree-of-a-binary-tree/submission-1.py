# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1==None or root2==None:
            return False
        else:
            if root1.val==root2.val and self.isSametree(root1.left,root2.left) and self.isSametree(root1.right,root2.right):
                return True
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None and root==None:
            return True
        elif subRoot==None or root==None:
            return False
        else:
            if self.isSametree(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot):
                return True
            return False
        
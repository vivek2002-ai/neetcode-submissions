# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 0
        root.val = 1
        myqueue = deque([root])
        while myqueue:
            node = myqueue.popleft()
            depth = node.val
            if node.left:
                node.left.val = depth + 1
                myqueue.append(node.left)
            if node.right:
                node.right.val = depth + 1
                myqueue.append(node.right)
        return depth

        
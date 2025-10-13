#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q is None or p is None:
            return q is p
        return self.f(p.right,q.left) and self.f(p.left,q.right) and p.val==q.val
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.f(root.left,root.right)
# @lc code=end


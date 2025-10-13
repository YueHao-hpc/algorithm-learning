#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node,depth):
            if node is None:
                return
            if depth==len(ans):
                ans.append(node.val)
            f(node.right,depth+1)
            f(node.left,depth+1)
        f(root,0)
        return ans
# @lc code=end


#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root == None:
        #     return 0
        # l_depth=self.maxDepth(root.left)
        # r_depth=self.maxDepth(root.right)
        # return max(l_depth,r_depth)+1
        ans = 0
        def f(node,cnt):
            if node == None:
                return
            cnt+=1
            nonlocal ans
            ans = max(cnt,ans)
            f(node.left,cnt)
            f(node.right,cnt)
            
        f(root,0)
        return ans
# @lc code=end


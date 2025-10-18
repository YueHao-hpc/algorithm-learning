#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        if n == 0:
            return []
        def dfs(i):
            if i == n:
                ans.append(path.copy())
            for j in range(i,n):
                
            

# @lc code=end


#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            d = k - len(path)
            if i < d:
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i,0,-1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans


# @lc code=end


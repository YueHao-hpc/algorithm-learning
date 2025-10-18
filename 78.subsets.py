#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        path = []
        if n == 0:
            return []
        def dfs(i):
            ans.append(path.copy())
            if i == n:
                return
            for j in range(i,n):
                
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans
# @lc code=end


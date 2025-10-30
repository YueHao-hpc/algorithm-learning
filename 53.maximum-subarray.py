#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        for num in nums[1:]:
            cur = max(num,num+cur)
            ans = max(cur,ans)
        return ans
                 
# @lc code=end


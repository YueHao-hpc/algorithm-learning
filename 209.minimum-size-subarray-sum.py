#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans=n+1
        sum=0
        left=0
        for right,x in enumerate(nums):
            sum+=x
            while sum-nums[left]>=target:
                sum-=nums[left]
                left+=1
            if sum>=target:
                ans=min(ans,right-left+1)
        return ans if ans<=n else 0
# @lc code=end


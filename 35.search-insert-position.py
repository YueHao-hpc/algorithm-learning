#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = bisect.bisect_left(nums,target)
        nums.insert(k,target)
        return k

         
# @lc code=end


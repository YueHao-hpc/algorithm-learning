#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,num in enumerate(nums):
            res = target - num
            if res in dict:
                return [i,dict[res]]
            else:
                dict[num]=i
        
# @lc code=end


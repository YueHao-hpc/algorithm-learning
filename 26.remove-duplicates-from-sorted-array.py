#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        slow = 0
        quick = 0
        while quick!=len(nums):
            if nums[slow] != nums[quick]:
                slow+=1
                nums[slow]= nums[quick]
            quick+=1
        return slow+1

        
# @lc code=end


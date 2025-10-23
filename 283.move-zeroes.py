#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        slow = 0
        for quick in range(0,len(nums)):
            if nums[quick]!=0:
                nums[slow]=nums[quick]
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0
        
# @lc code=end


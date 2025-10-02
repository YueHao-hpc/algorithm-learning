#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return[-1,-1]
        left = 0
        right = len(nums)-1
        if nums[left]>target:
            return[-1,-1]
        if nums[right]<target:
            return[-1,-1]
        while left<=right:
            medium = (left+right)//2
            if nums[medium]<target:
                left=medium+1
            else:
                right=medium-1
        start=left
        if nums[start]!=target:
            return[-1,-1]
        left = 0
        right = len(nums)-1
        while left<=right:
            medium = (left+right)//2
            if nums[medium]>target:
                right=medium-1
            else:
                left=medium+1
        end=right
        return [start,end]
# @lc code=end


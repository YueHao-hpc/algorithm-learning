#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n-1
        mid = (l+r)//2
        while l<=r:
            if nums[mid]>target:
                r = mid-1
                mid = (l+r)//2
            elif nums[mid]<target:
                l = mid+1
                mid = (l+r)//2
            else:
                return mid
        return -1
            
# @lc code=end


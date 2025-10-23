#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        right = len(nums)-1
        left = 0
        while left<=right:
            if nums[left] == val:
                nums[left]=nums[right]
                right-=1
                
            else:
                left+=1
                k+=1
        return k
# @lc code=end


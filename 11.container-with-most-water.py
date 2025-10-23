#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        size = (right-left)*min(height[left],height[right])
        while left<right:
            if height[left]<=height[right]:
                left+=1
                current_height = min(height[left],height[right])
                size = max(size,(right-left)*current_height)
            else:
                right-=1
                current_height = min(height[left],height[right])
                size = max(size,(right-left)*current_height)
        return size

# @lc code=end


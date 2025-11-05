#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights+[0]):
            while stack and heights[stack[-1]]>=h:
                mid = stack.pop()
                height = heights[mid]
                left = stack[-1] if stack else -1
                right = i
                width = right-left-1
                max_area = max(max_area,width*height)
            stack.append(i)
        return max_area

# @lc code=end


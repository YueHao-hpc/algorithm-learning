#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        dict = {}
        for i,ch in enumerate(s):
            if ch in dict:
                left = max(left,dict[ch]+1)
            
            dict[ch] = i
            ans = max(ans,i-left+1)
        return ans
            

                
# @lc code=end


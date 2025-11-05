#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans = 0
        pre=0
        suf=n-1
        pre_max=0
        suf_max=0
        while pre<=suf:
            pre_max = max(pre_max,height[pre])
            suf_max = max(suf_max,height[suf])
            if pre_max<suf_max:
                ans+=pre_max-height[pre]
                pre+=1
            else:
                ans+=suf_max-height[suf]
                suf-=1
        return ans

                
# @lc code=end


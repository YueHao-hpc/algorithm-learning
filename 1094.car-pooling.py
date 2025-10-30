#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff_array = [0]*1001
        now = 0
        for trip in trips:
            diff_array[trip[1]]+=trip[0]
            diff_array[trip[2]]-=trip[0]
        for num in diff_array:
            now+=num
            if now>capacity:
                return False
        return True

        
        
# @lc code=end


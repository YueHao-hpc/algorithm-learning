#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while True:
            s = numbers[left]+numbers[right]
            if s== target:
                break
            if s>target:
                right-=1
            if s<target:
                left+=1
        return[left+1,right+1]
# @lc code=end


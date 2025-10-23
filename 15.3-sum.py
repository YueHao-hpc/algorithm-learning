#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0,n-2):
            left = i+1
            right = n-1
            if nums[i]>0:
                break
            if nums[n-1]<0:
                break
            if i>0 and nums[i-1]==nums[i]:
                continue
            while left < right:
                current_sum = nums[left] + nums[right]
                target = -nums[i]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
            
            


        return ans
                


# @lc code=end

/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.empty())
        {
            return 0;
        }
        int slow = 0;
        for(int fast = 0; fast<nums.size(); fast++){
            if(nums[fast]  != val){
                nums[slow] = nums[fast];
                slow++;
            }
        }
        return slow;
        
    }
};
// @lc code=end


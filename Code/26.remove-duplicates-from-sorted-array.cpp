/*
 * @lc app=leetcode id=26 lang=cpp
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
        {
            return 0;
        }
        else {
            int slow = 1;
            for (int fast = 1; fast < nums.size(); ++fast )
            {
                if(nums[fast] != nums[slow-1]){
                    nums[slow] = nums[fast];
                    ++slow;
                };
            }
            return slow;
        }
    }
};
// @lc code=end


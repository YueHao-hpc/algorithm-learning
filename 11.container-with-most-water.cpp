/*
 * @lc app=leetcode id=11 lang=cpp
 *
 * [11] Container With Most Water
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size()-1;
        int size = 0;
        while (left<right)
        {
            int h = min(height[left],height[right]);
            int w = right - left;
            size = max(size,h*w); 
            if (height[left]<height[right])
            {
                left++;
            }
            else{
                right--;
            }
            
        }
        return size;
        
        
    }
};
// @lc code=end


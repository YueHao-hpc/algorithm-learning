#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        Counter_s = Counter(s)
        pairs = sorted(Counter_s.items(),key=lambda x:x[1],reverse=True)
        return ''.join(ch*val for ch,val in pairs)
# @lc code=end


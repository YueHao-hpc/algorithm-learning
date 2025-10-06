#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # i = s.split()
        # res = []
        # for j in i:
        #     res.append(j[::-1])
        # return ' '.join(res)
        return ' '.join(word[::-1] for word in s.split())
# @lc code=end


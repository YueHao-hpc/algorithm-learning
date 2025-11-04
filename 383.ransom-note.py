#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Counter_ransomNote = Counter(ransomNote)
        Counter_magazine = Counter(magazine)
        return True if Counter_magazine>=Counter_ransomNote else False

# @lc code=end


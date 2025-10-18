#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
Mapping = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = ['']*n
        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return 
            else:
                for ch in Mapping[int(digits[i])]:
                    path[i] = ch
                    dfs(i+1)
        dfs(0)
        return ans
# @lc code=end


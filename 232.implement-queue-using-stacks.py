#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)


    def pop(self) -> int:
        if not self.out_st:
            while self.in_st:
                out = self.in_st.pop()
                self.out_st.append(out) 
        res = self.out_st.pop()
        return res
    def peek(self) -> int:
        if self.out_st:
            return self.out_st[-1]
        else:
            while self.in_st:
                out = self.in_st.pop()
                self.out_st.append(out)
            return self.out_st[-1]
    def empty(self) -> bool:
        return len(self.in_st)==0 and len(self.out_st)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


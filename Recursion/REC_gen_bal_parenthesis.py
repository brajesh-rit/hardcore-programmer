"""
https://www.interviewbit.com/problems/generate-all-parentheses-ii/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""

class Solution():
    result = []
    def solve(self,open,close,output):
        if open == 0 and close == 0:
            self.result.append(output)
            return
        if open > 0:
            op1 = output + '('
            #open -= 1   never do this
            self.solve(open - 1,close,op1)
        if close > open:
            op2 = output + ')'
            self.solve(open, close -1, op2)
        return


    def generateParenthesis(self, A):
        output = ""
        self.solve(A, A, output)
        return self.result

count = 3
result = Solution()
print(result.generateParenthesis(count))
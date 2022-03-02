#https://practice.geeksforgeeks.org/problems/permutation-with-spaces3627/1
#Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.
# The output should be printed in sorted increasing order of strings
# Don't run successful due to plateform error
class Solution:
    result = []
    def solve(self,str,output):
        if str == "":
            self.result.append(output)
            return
        op1 = output + str[0]
        op2 = output + " " + str[0]
        self.solve(str[1:],op1)
        self.solve(str[1:],op2)
        return

    def permutation (self, str):
        output = str[0]
        self.solve(str[1:],output)
        return self.result




str = "LW"
result = Solution()
print(result.permutation(str))
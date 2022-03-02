#Print all unique subsequence of given string
class Solution:
    result = []
    def printSubseq(self,str,output):
        if str =="":
            self.result.append(output)
            return
        op1 = output
        op2 = output + str[0]
        self.printSubseq(str[1:],op1)
        self.printSubseq(str[1:],op2)
        return
    #https://leetcode.com/problems/subsets-ii/
    def printsubset(self,arr,output):
        if arr == []:
            self.result.append(output)
            return
        op1 = list(output)
        op2 = list(output)
        op2.append(arr[0])
        self.printsubset(arr[1:],op1)
        self.printsubset(arr[1:],op2)
        return

#str = "aab"
#output = ""
#Solution().printSubseq(str,output)
#uniq = set(Solution().result) # just convert to unique array
#print(uniq)                  # set datastructure is sort itself.
#print(uniq.sort())

arr = [2,2,1]
output = []
Solution().printsubset(arr,output)
result = Solution().result
uniq = [list(y) for y in set(tuple(x) for x in result)]
print(uniq)

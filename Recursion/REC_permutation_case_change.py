#https://www.geeksforgeeks.org/permute-string-changing-case/
#Print all permutations of a string keeping the sequence but changing cases.
#Input : ab
#Output : AB Ab ab aB
class Solution():
    result = []
    def solve1(self, str, nbr):
        if nbr == len(str):
            self.result.append(str)
            return
        op1 = str
        op2 = str[:nbr] + str[nbr].upper() + str[nbr+1:]
        self.solve1(op1,nbr+1)
        self.solve1(op2,nbr+1)
        return

    def permute1(self, inp):
        self.solve1(inp, 0)
        return self.result
    #I have return above program because I confuse the intermediate tree output is final output and I taken the number
    # parameter
    def solve2(self,str,output):
        if str == "":
            self.result.append(output)
            return
        op1 = output + str[0]
        op2 = output + str[0].upper()
        self.solve2( str[1:],op1)
        self.solve2(str[1:], op2)
        return
    def permute(self, inp):
        self.solve2(inp, "")
        return self.result

    def solve(self, str, output):
        if str == "":
            self.result.append(output)
            return
        while str[0].isnumeric():
            output = output + str[0]
            str = str[1:]
            if str == "":  #   this code is only for numeric is in last
                self.result.append(output)
                return

        op1 = output + str[0].lower()
        op2 = output + str[0].upper()
        self.solve(str[1:], op1)
        self.solve(str[1:], op2)
        return

    def letterCase(self, str):
        output = ""
        while str[0].isnumeric():
            output = output + str[0]
            str = str[1:]
        self.solve(str, output)
        return self.result

inp = "12aB234c"
result = Solution()
print(result.letterCase(inp))
class Solution:
    def printShortestSuperSeq(self,X , Y):
        xLen = len(X)
        yLen = len(Y)
        mem = [[-1 for x in range(yLen + 1)] for x in range(xLen + 1)]
        for row in range(xLen + 1):
            for col in range(yLen + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,xLen + 1):
            for col in range(1,yLen + 1):
                if X[row -1] == Y[col - 1]:
                    mem[row][col] = 1 + mem[row -1][col - 1]
                else:
                    mem[row][col] = max(mem[row - 1][col], mem[row][col - 1])

        #print
        row = xLen
        col = yLen
        str = ""
        while (row > 0 and col > 0):
            if X[row - 1]== Y[col - 1]:
                str = str + X[row - 1]
                row -= 1
                col -= 1
            else:
                if mem[row][col - 1] >= mem[row - 1][col]:  # focus on = sign as well if both equal then any place movement is fine
                    str = str + Y[col - 1]
                    col -= 1
                elif mem[row][col - 1] < mem[row - 1][col]:
                    str = str + X[row - 1]                   # beware of decreasing of row it should be after saving the character in current shell
                    row -= 1

        while (row > 0):
            str = str + X[row - 1]
            row -= 1
        while (col > 0):
            str = str + Y[col - 1]
            col -= 1
        output = str[::-1]
        return  output

X = "AGGTAB"
Y = "GXTXAYB"
result = Solution()
print(result.printShortestSuperSeq(X, Y))
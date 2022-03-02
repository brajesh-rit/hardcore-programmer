class Solution:
    def all_longest_common_subsequences(self, s, t):
        sLen = len(s) # row
        tLen = len(t)  # column
        mem = [[-1 for x in range(tLen + 1)] for x in range(sLen + 1)]

        for row in range(sLen + 1):
            for col in range(tLen + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,sLen+ 1):
            for col in range(1,tLen + 1):
                if s[row -1] == t[col - 1]:
                    mem[row][col] = mem[row - 1][col - 1] + 1
                else:
                    mem[row][col] =  max(mem[row -1][col], mem[row][col - 1])
        row = sLen
        col = tLen
        output = ''
        while (row > 0 and col > 0):   # should be and because any row or col hit to 0 come out the loop
            if s[row -1] == t[col -1]:
                output = output + s[row - 1]
                row -= 1
                col -= 1
            else:
                if mem[row][col - 1] > mem[row - 1][col]:
                    col -= 1                  # whichever greater row or col same one will be decrease by one
                else:
                    row -= 1
        output = output[::-1]

        return output

s = 'acbcf'
t = 'abcdaf'
result = Solution()
print(result.all_longest_common_subsequences( s ,t ))



#https://leetcode.com/problems/super-egg-drop/
# find threshold/critical floor
# with minimum number of moves
# from where dropped egg will not break
class Solution:
    def superEggDrop1(self, e, f):
        if f == 1 or f == 0:
            return f
        if e == 1:
            return f
        out = float('inf')

        for x in range(1, f + 1): # f + 1 because range exclude the second parameter by 1
            res = 1 + max(self.superEggDrop(e - 1, x - 1),  self.superEggDrop(e, f - x))
            out = min(out , res)
        return out
    mem = {}
    def superEggDrop1(self, e, f):
        key = str(e) + ',' + str(f)
        if key in self.mem:
            return self.mem[key]

        if f == 1 or f == 0:
            self.mem[key] = f
            return f
        if e == 1:
            self.mem[key] = f
            return f
        out = float('inf')

        for x in range(1, f + 1): # f + 1 because range exclude the second parameter by 1
            res = 1 + max(self.superEggDrop(e - 1, x - 1),  self.superEggDrop(e, f - x))
            out = min(out , res)
        self.mem[key] = out
        return out

    # more optimize through store value seperatly in recursive call
    # time limit exceeded
    def superEggDrop(self, e, f):
        key = str(e) + ',' + str(f)
        if key in self.mem:
            return self.mem[key]

        if f == 1 or f == 0:
            self.mem[key] = f
            return f
        if e == 1:
            self.mem[key] = f
            return f
        out = float('inf')

        for x in range(1, f + 1): # f + 1 because range exclude the second parameter by 1
            lkey = str(e-1)+','+str(x-1)
            if lkey in self.mem:
                low = self.mem[lkey]
            else:
                low = self.superEggDrop(e - 1, x - 1)
                self.mem[lkey] = low
            hkey = str(e) +','+ str(f-x)
            if hkey in self.mem:
                high = self.mem[hkey]
            else:
                high = self.superEggDrop(e, f - x)
                self.mem[hkey] = high
            res = 1 +  max(low , high)
            out = min(out , res)
        self.mem[key] = out
        return out


    # Below is wrong code not working
    def superEggDrop1(self, e, f):
        mem = [[-1 for x in range(f+1)] for x in range(e+1)]

        for row in range(e+1):
            for col in range(f+1):
                if col == 1 or col == 0:
                    mem[row][col] = col
                if row == 1:
                    mem[row][col] = col
        out = float('inf')
        for row in range(e+1):
            for col in range(f+1):
                for x in range(1, f + 1): # f + 1 because range exclude the second parameter by 1
                    res = 1 + max(mem[row - 1][x - 1],  mem[row][col - x])
                    out = min(out , res)
                mem[row][col] = out
        return mem[e][f]

    #copy paste form leetcode don't follow
    def superEggDrop1(self, e, f):
        dp = [[0 for i in range(e+1)] for i in range(f + 1)]
        for m in range(1, f + 1):
            for k in range(1, e + 1):
                print('dp[{0}][{1}] = dp[{0} - 1][{1} - 1] + dp[{0} - 1][{1}] + 1'.format(m,k))
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][e] >= f:
               return m

e = 3  # no of egg given for test
f = 7 # no of floor given
result = Solution()
print(result.superEggDrop(e,f))
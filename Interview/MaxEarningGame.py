def MaxEarnGame(W, wt, val, game, n):

   if n == 0 or W == 0:
       return 0

   if (wt[n - 1] > W):
       print (game[n-1])
       result = MaxEarnGame(W, wt, val, game, n - 1)
       return result
   else:
       print('else')
       print(game[n - 1])
       return max(
                   val[n - 1] + MaxEarnGame( W - wt[n - 1], wt, val, game, n - 1),
                   MaxEarnGame(W, wt, val,game, n - 1))

def knapSack(W,wt,val,n):
    # intialized with -1 of all the two dimension array
    mem = [[-1 for i in range(W+1)]for i in range(n+1)]
    # intialized the base condition
    for row in range(n+1):
        for col in range(W+1):
            if row == 0 or col ==0:
                mem[row][col] = 0
    # choice diagram code
    for row in range(1,n+1):
        for col in range(1, W+1):
            if wt[row-1] > col:
                mem[row][col] = mem[row -1][col]
            else:
                mem[row][col] = max(val[row - 1] + mem[row-1][col-wt[row-1]], mem[row-1][col])
    print(val[row - 1] + mem[row - 1][col - wt[row - 1]], mem[row - 1][col])
    return mem[n][W]


val = [1,4,5,7]
wt = [1,3,4,5]
W = 7
n = len(val)

# val = [250,280,150,120,200,100,300,350,110,90]
# wt = [75,45,30,35,30,15,60,90,20,10]
# W = 120
# n = len(val)
# game = ['Pac-man','Speed Racer','Pump it Up','Space Invaders','Mario Bros','Mortal Kombat','Atari Breakout','Super Tetris','Star Wars','Street Fighter II']

#print(MaxEarnGame(W, wt, val, game, n))
print(knapSack(W, wt, val, n))
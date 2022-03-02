class Solution:
    def lenOfLongSubarr1 (self, A, N, K) :
        end = 0
        start = 0
        sum = 0
        max_win = 0
        while(end < len(A)):
            sum = sum + A[end]
            if sum < K:
                end = end + 1
            elif sum == K:
                max_win = max(max_win,end-start + 1)
                end = end + 1
            elif sum > K:
                sum = sum - A[start]
                start = start + 1
                end = end + 1
        return max_win

    def lenOfLongSubarr (self, A, N, K) :
        end = 0
        start = 0
        sum = 0
        max_win = 0
        while(end < len(A)):
            sum = sum + A[end]
            if sum < K:
                end = end + 1
            elif sum == K:
                max_win = max(max_win,end-start + 1)
                end = end + 1
            elif sum > K:
                while sum > K:
                    sum = sum - A[start]
                    start = start + 1
                end = end + 1
        return max_win

result = Solution()
print (result.lenOfLongSubarr( [-1, 2, 3], 6, 6))
print (result.lenOfLongSubarr( [-13 ,0 ,6 ,15 ,16 ,2 ,15 ,-12 ,17 ,-16 ,0 ,-3 ,19 ,-3 ,2 ,-9, -6], 6, 15))

#I want to learn desc heap arr
import heapq
class Solution:
    def heap_asc(self, arr):
        harr = []
        for i in range(len(arr)):
            heapq.heappush(harr, arr[i] * -1)
        for i in range(len(harr)):
            print(heapq.heappop(harr) * -1)

res = Solution()

arr = [10, 2, 14, 4, 7, 6]
res.heap_asc(arr)

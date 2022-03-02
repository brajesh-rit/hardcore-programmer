#Print the elements of an array in the increasing frequency if 2 numbers have same frequency then print the one which came first.
import heapq
class Solution:
    def feqSort(self,arr):
        dic = {}
        for key in arr:
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1
        harr = []
        for key in dic:
            heapq.heappush(harr,(dic[key] * -1, key))
        result = []
        for i in range(len(harr)):
            val = heapq.heappop(harr)
            for i in range(val[0] * -1):
                result.append(val[1])
        return result

result = Solution()
arr = [2, 5, 2, 8, 5, 6, 8, 8]
print(result.feqSort(arr))


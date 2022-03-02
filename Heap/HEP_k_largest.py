#https://practice.geeksforgeeks.org/problems/k-largest-elements3736/1
#Given an array of N positive integers, print k largest elements from the array.
import heapq
class Solution(object):
    def kLargest(self, nums, n, k):
        queue = []
        for i in range(len(nums)):
            #val = nums[i]*(-1)
            heapq.heappush(queue, nums[i])
            if len(queue) > k:
                heapq.heappop(queue)
        res = [i for i in queue]
        res = sorted(res, reverse = True)
        return res
    
result = Solution()
arr = [1,23,12,9,30,2,50]
n = len(arr)
k = 3
print(result.kLargest(arr,n, k))

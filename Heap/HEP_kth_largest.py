#https://leetcode.com/problems/kth-largest-element-in-an-array/
#Given an integer array nums and an integer k, return the kth largest element in the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
#Successfully implement in leetcode
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):

        queue = []
        for i in range(len(nums)):
            heapq.heappush(queue, nums[i])
            if len(queue) > k:
                heapq.heappop(queue)
        return heapq.heappop(queue)

nums = [3,2,1,5,6,4]
k = 2
result = Solution()
print(result.findKthLargest(nums,k))
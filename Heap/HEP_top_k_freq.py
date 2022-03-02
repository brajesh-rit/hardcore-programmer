"""
#https://leetcode.com/problems/top-k-frequent-elements/
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# successful submit is leetcode
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""



import heapq
class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        harr = []
        for key in dic:
            heapq.heappush(harr,(dic[key],key))
            if len(harr) > k:
                heapq.heappop(harr)
        res = []
        for i in range(len(harr)):
            val = heapq.heappop(harr)
            res.append(val[1])
        return res

result = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(result.topKFrequent(nums,k))
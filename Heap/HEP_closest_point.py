"""
https://leetcode.com/problems/k-closest-points-to-origin/
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""



import heapq, math
class Solution(object):
    def kClosest(self, points, k):
        harr = []
        for i in range(len(points)):
            # we can remove sqrt because order does not matter for sqrt just of saving calculattion
            heapq.heappush(harr,((points[i][0]**2 + points[i][1]**2) * -1,i))
            if len(harr) > k:
                heapq.heappop(harr)
        res = []
        for i in range(k):
            val = heapq.heappop(harr)
            res.append(points[val[1]])
        return res

points = [[1, 3], [-2, 2]]
k = 1
result = Solution()
print(result.kClosest(points,k))
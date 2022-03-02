"""
https://www.interviewbit.com/problems/sliding-window-maximum/#
Given an array of integers A.  There is a sliding window of size B which

is moving from the very left of the array to the very right.

You can only see the w numbers in the window. Each time the sliding window moves

rightwards by one position. You have to find the maximum for each window.

The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1  3  -1] -3  5  3  6  7	3
1 [3  -1  -3] 5  3  6  7	3
1  3 [-1  -3  5] 3  6  7	5
1  3  -1 [-3  5  3] 6  7	5
1  3  -1  -3 [5  3  6] 7	6
1  3  -1  -3  5 [3  6  7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.


"""
class Solution(object):
    # Below brute force return maximum limit time is increase error
    def maxSlidingWindow1(self, nums, k):
        max_val = nums[0]
        result = []
        for i in range(len(nums) - k + 1): # always add one because last data is missing
            max_val =nums[i]
            for j in range(i,k+i):
                max_val = max(max_val,nums[j])
            result.append(max_val)
        return result

    def maxSlidingWindow(self, nums, k):
        start = 0
        end = 0
        result = []
        queue = []
        while end < k:
            if len(queue) != 0:
                i = 0
                while i < len(queue):
                    if queue[i] < nums[end]:
                        queue.pop(i)
                    else:
                        i = i + 1
            queue.append(nums[end])
            end = end + 1
        end = end - 1
        result.append(queue[0])
        while end < len(nums) - 1:
            if queue[0] == nums[start]:
                queue.pop(0)
            start = start + 1
            end = end + 1
            if len(queue) != 0:
                i = 0
                while i < len(queue):
                    if queue[i] < nums[end]:
                        queue.pop(i)
                    else:
                        i = i + 1
            queue.append(nums[end])
            result.append(queue[0])
        return result

result = Solution()
print (result.maxSlidingWindow( [1,3,1,2,0,5], 3))  #[3,3,2,5]  [3,3,1,5]
print (result.maxSlidingWindow( [1,3,-1,-3,5,3,6,7], 3))
print (result.maxSlidingWindow( [1], 1))
print (result.maxSlidingWindow( [1, -1], 1))
print (result.maxSlidingWindow( [9, 11], 2))
print (result.maxSlidingWindow( [4, -2], 2))
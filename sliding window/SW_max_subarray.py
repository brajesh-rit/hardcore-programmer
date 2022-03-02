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
class Solution:
    def slidingMaximum(self, nums, size):
        leng = len(nums)
        start = 0
        end = 0
        q = []
        ans = []
        while end < leng:
            qlen = len(q)
            i = 0
            if qlen != 0:
                while i < qlen:
                    if q[i] < nums[end]:
                        q.pop(i)
                    else:
                        i += 1
            q.append(nums[end])
            if (end-start+1) == size:
                ans.append(q[0])
                if q[0] == nums[start]:
                    q.pop(0)
                start += 1
            end += 1
        return ans

test = Solution()
# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# size = 3
nums = [1]
size = 1
print(test.slidingMaximum(nums,size))

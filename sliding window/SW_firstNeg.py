"""
https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#
First negative integer in every window of size k
Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

Example 1:

Input :
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output :
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
"""


def firstNegative1(self, nums, size):
    result = []
    getResult = False
    for start in range(len(nums) - (size - 1)):  # take care of window size end point
        for win_start in range(start, (start + size)):
            if nums[win_start] < 0:
                result.append(nums[win_start])
                getResult = True
                break
            else:  # always think about the else part
                getResult = False
        if not getResult:
            result.append(0)
    return result

def printFirstNegativeInteger(len_arr,nums, size ):
    start = 0
    end = 0
    ans = []
    q = []
    while end < len_arr:
        if nums[end] < 0:
            q.append(nums[end])
        if (end-start+1) == size:
            if len(q) != 0:
                ans.append(q[0])
            else:
                ans.append(0)
            if nums[start] < 0:
                q.pop(0)
            start += 1
        end += 1

    return ans

nums = [-8, 2, 3, -6, 10]
len_arr = len(nums)
size = 2
print(printFirstNegativeInteger(len_arr,nums,size))

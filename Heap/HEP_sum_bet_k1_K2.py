"""
Below question is not from any coding plateform

Given an array of integers and two numbers k1 and k2. Find the sum of all elements between given two
k1’th and k2’th smallest elements of the array. It may  be assumed that all elements of array are distinct.
k2 > k1
Example :
Input : arr[] = {20, 8, 22, 4, 12, 10, 14},  k1 = 3,  k2 = 6
Output : 26
         3rd smallest element is 10. 6th smallest element
         is 20. Sum of all element between k1 & k2 in the sorted arr arr = [4,8,10,12,14,20,22] is
         12 + 14 = 26
"""
import heapq
def sumBetK1andK2(arr,k1,k2):
    harr = []
    for val in arr:
        heapq.heappush(harr,val * - 1)
    while len(harr) >= k1:
        if len(harr) == k2:
            k2Val = heapq.heappop(harr) * -1
        elif len(harr) == k1:
            k1Val = heapq.heappop(harr) * -1
        else:
            heapq.heappop(harr)
    ans = 0
    for i in arr:
        if k1Val < i and i < k2Val:
            ans = ans + i
    return ans
arr = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6
print(sumBetK1andK2(arr, k1,k2))
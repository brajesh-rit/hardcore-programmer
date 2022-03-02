"""
https://www.geeksforgeeks.org/trapping-rain-water/
https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1
Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1,
compute how much water can be trapped between the blocks during the rainy season.

Example 1:

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above
block of height 4 is 3 units and above
block of height 0 is 7 units. So, the
total unit of water trapped is 10 units.

"""

#https://www.geeksforgeeks.org/trapping-rain-water/
#Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
class Solution:
    def trappingWater(self, arr,n):

            #intialized array of given array
            #This is helpful for not append the array
            left = [0] * n
            right = [0] * n

            # Initialize result
            water = 0

            #Intialized the first value of the array
            left[0] = arr[0]
            #Transversed left to right from 1 because 0 is store above
            for i in range(1, n):
                left[i] = max(left[i - 1], arr[i])

            #Intialized from right side of the array
            right[n - 1] = arr[n - 1]
            #start from n-2 till -1 because n-1 is stored and go till zero
            for i in range(n - 2, -1, -1):
                right[i] = max(right[i + 1], arr[i])

            # Below is actual calcualtion
            for i in range(0, n):
                water += min(left[i], right[i]) - arr[i]

            return water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
Test = Solution()
print(Test.trappingWater(arr,n))
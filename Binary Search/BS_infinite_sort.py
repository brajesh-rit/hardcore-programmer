"""
https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/
Find position of an element in a sorted array of infinite numbers

Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
Source: Amazon Interview Experience.
Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
->if it is greater than high index element then copy high index in low index and double the high index.
->if it is smaller, then apply binary search on high and low indices found.


class Solution:
    def indexOfFirstOne(self, arr, low, high):
        low = 0
        high = len(arr) - 1
        x = 1
        res = -1
        while low <= high:

            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1

            elif arr[mid] > x:
                high = mid - 1

            else:
                res =  mid
                high =  mid -1  # above two line is change here if you want first occurence
        return res

    def posOfFirstOne(self, arr):

        low, high  = 0, 1
        while arr[high] == 0:
            low = high  # store previous high
            high = 2 * high  # double high index

        # at this point we have updated low and high indices,
        # thus use binary search between them
        return self.indexOfFirstOne(arr, low, high)

# Your code here
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,1, 1,1, 1,1, 1,1]


result = Solution()
print(result.posOfFirstOne(arr))
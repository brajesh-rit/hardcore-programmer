#https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1
#Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.
class Solution:
    def count(self, arr,n,x):
        def first(arr,x):
            low = 0
            high = len(arr) - 1
            mid = 0
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

        def last(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0
            res = -1
            while low <= high:

                mid = (high + low) // 2

                if arr[mid] < x:
                    low = mid + 1

                elif arr[mid] > x:
                    high = mid - 1

                else:
                    res = mid
                    low = mid + 1  # above two line is change here if you want last occurence
            return res

        Fval = first(arr,x)
        lval = last(arr,x)
        if Fval != -1:
            return lval - Fval + 1
        else:
            return 0
n = 7
x = 20
arr = [1,1,2,2,2,2,3 ]
result = Solution()
print(result.count(arr,n,x))
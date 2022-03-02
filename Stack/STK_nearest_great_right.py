"""
https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
Next Greater Element
Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element
 of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1.
For example, next greater of the last element is always -1.

Example 1:

Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.
Example 2:

Input:
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to
6 is 8, for 8 there is no larger elements
hence it is -1, for 0 it is 1 , for 1 it
is 3 and then for 3 there is no larger
element on right and hence -1.
"""
class Solution:
    def nextLargerElement(self, arr,n):
        s = []
        ans = []
        for i in range(n-1,-1,-1):  # check in reverse count down last is -1 otherwise it will not count 0
            if len(s) == 0:    # we can take if not s since blank object also known as false
                ans.append(-1)
            else:
                while len(s) > 0 and s[len(s) - 1] <= arr[i]: #stack end of array is top remember it
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[len(s) - 1])
            s.append(arr[i])
        ans = ans[::-1]
        return ans


arr = [1, 3, 2, 4]
n = len(arr)
print(Solution().nextLargerElement(arr,n))
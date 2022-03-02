"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Given a characters array letters that is sorted in accending order and a character target,
return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"
Example 4:

Input: letters = ["c","f","j"], target = "g"
Output: "j"
Example 5:

Input: letters = ["c","f","j"], target = "j"
Output: "c"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
successfully submit
"""

class Solution:
    def nextGreatestLetter(self, arr, key):
        low = 0
        high = len(arr) - 1

        # If last element is smaller than x
        if key >= arr[high]:
            return arr[low]      # agar key high se bhi bhda hai to round ho jayga aur low value return karega
        elif key < arr[low]:
            return arr[low]

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == key:
                low = mid + 1    # diff through ceil code if found even after go for next smallest number
            elif arr[mid] < key:
                low = mid  + 1
            elif arr[mid] > key:
                res = mid
                high = mid - 1
        return arr[res]
# Your code here
# arr = ['a','b','c','d','e','f']
# N = 7
# x = 'd'
# arr = ["c","f","j"]
# x = 'a'

arr = ["c","f","j"]
x = 'j'
result = Solution()
print(result.nextGreatestLetter(arr, x))
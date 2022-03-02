"""
https://practice.geeksforgeeks.org/problems/game-of-death-in-a-circle1840/1
There are n people standing in a circle (numbered clockwise 1 to n) waiting to be executed.
The counting begins at point 1 in the circle and proceeds around the circle in a fixed direction (clockwise).
In each step, a certain number of people are skipped and the next person is executed.
The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed),
 until only the last person remains, who is given freedom.
Given the total number of persons n and a number k which indicates that k-1
persons are skipped and kth person is killed in circle.
The task is to choose the place in the initial circle so that you are the last one remaining and so survive.
Example 1:

Input:
n = 2, k = 1
Output:
2
Explanation:
Here, n = 2 and k = 1, then safe position is
2 as the person at 1st position will be killed.
Example 2:

Input:
n = 4, k = 2
Output:
1
Explanation:
The safe position is 1.
"""

class Solution:
    def solve(self, arr, pos, k):
        if len(arr) == 1:
            return arr[0]
        pos = (pos + k)% len(arr)
        arr.pop(pos)
        return self.solve(arr,pos, k)

    def safePos(self, n, k):
        k -= 1             #in array position is start from 0 index so decrease k by 1 for easy calculation
        arr = [i+1 for i in range(n)]
        pos = 0             # start from first element of array
        return self.solve(arr, pos, k)

n = 40
k = 7
result = Solution()
print(result.safePos(n, k))
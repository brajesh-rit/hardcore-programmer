"""
https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome
Determine the fewest cuts needed for a palindrome partitioning of a given string.
For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are “a|babbbab|b|ababa”.
"""
class Solution:
    def palindromicPartition(self, arr):
        def isPlaindrome(str):
            return str == str[::-1]

        def solve(arr,i, j):

            if i >= j :
                return 0
            if isPlaindrome(arr[i:j+1]):
                return 0
            minVal = float('inf')
            for k in range(i,j):
                tmp =  1+ solve(arr,i,k) + solve(arr, k+1,j)
                minVal = min(minVal, tmp)
            return minVal

        def solve2(arr,i,j):
            leng =  len(arr)
            mem = [[0 for _ in range(j)] for _ in range(i)]
            # not need to write to fill diagonal to zero
            for d in range(1,leng):
                for row in range(2,n-2):
                    col = row - d
                    

        leng = len(arr)
        i = 0
        j = leng - 1
        return solve(arr,i, j)



test = Solution()
arr = "ababbbabbababa"
print(test.palindromicPartition(arr))
"""
https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1
Palindromic patitioning
Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of given string.


Example 1:

Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings
are "a", "babbbab", "b", "ababa".
Example 2:

Input: str = "aaabba"
Output: 1
Explaination: The substrings after 1
partitioning are "aa" and "abba".
"""
class Solution:
    def isPlindrom(self,arr):
        return arr == arr[::-1]

    def palindromicPartition1(self, arr , i , j):
        #Base condition
        #when i = j means it return one character
        #one charachter is palidrom hence no cut required hence return 0
        # i> j is invalid input hence return 0

        if  i >= j:
            return 0
        #Since arr is always pass same hence here slice the string according to i and j
        #why j+1 ? becuase second argument is excluded in slicing the string
        if self.isPlindrom(arr[i:j+1]):
            return 0

        result = float('inf')
        # why j-1 because k+1 value passing in second call, if k = j  second call  j+1, J tha is invalid
        # since range is taken max value - 1
        for k in range(i , j):
            # why adding 1 in cost? because function call return the cost of two string after partition,
            # but current one partition is happen hence we add the current cost as 1
            cost =  (1 + self.palindromicPartition(arr,i , k) +
                         self.palindromicPartition(arr, k+1, j))
            result = min(result,cost)
        return result

    mem = {}
    def palindromicPartition2(self, arr, i, j):
        key = str(i)+ ',' + str(j)
        if key in self.mem:
            return self.mem[key]

        if i >= j:
            return 0
        if self.isPlindrom(arr[i:j+1]):
            self.mem[key] = 0
            return 0

        result = float('inf')
        for k in range(i, j):
            cost = (1 + self.palindromicPartition(arr, i, k) +
                    self.palindromicPartition(arr, k + 1, j))
            result = min(result,cost)

        self.mem[key] = result
        return result

    #Below code is capture memory seperately
    def palindromicPartition3(self, arr, i, j):
        key = str(i)+ ',' + str(j)
        if key in self.mem:
            return self.mem[key]

        if i >= j:
            return 0
        if self.isPlindrom(arr[i:j+1]):
            self.mem[key] = 0
            return 0

        result = float('inf')
        for k in range(i, j):
            left_key = str(i)+ ',' + str(k)
            if left_key in self.mem:
                left_min = self.mem[left_key]
            else:
                left_min = self.palindromicPartition(arr, i, k)

            right_key = str(k + 1) + ',' + str(j)
            if right_key in self.mem:
                right_min = self.mem[right_key]
            else:
                right_min = self.palindromicPartition(arr, k + 1, j)

            cost = (1 + left_min + right_min  )
            result = min(result,cost)

        self.mem[key] = result
        return result

    #Do not focus 
    def palindromicPartition(self,arr):
        cut = [0 for i in range(len(arr))]
        palindrome = [[False for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            minCut = i;
            for j in range(i + 1):
                if (arr[i] == arr[j] and (i - j < 2 or palindrome[j + 1][i - 1])):
                    palindrome[j][i] = True;
                    minCut = min(minCut, 0 if j == 0 else (cut[j - 1] + 1));
            cut[i] = minCut;
        return cut[len(arr) - 1];


arr = 'aaabba'
n = len(arr)
result = Solution()
#i value start from 0(zero) j value end arr.length - 1
# mark zero in first place because arr start always from 0
#print(result.palindromicPartition(arr, 0 , n -1))
print(result.palindromicPartition(arr))
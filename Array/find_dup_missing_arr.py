#https://www.interviewbit.com/problems/repeat-and-missing-number-array/
#You are given a read only array of n integers from 1 to n.
#Each integer appears exactly once except A which appears twice and B which is missing.

class Solution:
    def repeatedNumber(self, arr):
        i = 0
        size = len(arr)
        while i < size:
            if arr[i] != arr[arr[i] - 1]:
                get = arr[i], arr[arr[i] - 1]
                arr[arr[i] - 1], arr[i] = get
            else:
                i += 1
        miss = []
        dup  = []
        for i in range(size):
            if arr[i] != i + 1:
                miss.append(i+1)
                dup.append(arr[i])
        print("Missing value ",miss)
        print("Duplicate value ", dup)
        return [dup[0],miss[0]]

result = Solution()
arr = [3, 1, 1, 5, 3]
print(result.repeatedNumber(arr))
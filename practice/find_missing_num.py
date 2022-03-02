"""
https://www.geeksforgeeks.org/python-find-missing-numbers-in-a-sorted-list-range/
Given a range of sorted list of integers with some integers missing in between, write a Python program to find all the missing integers.
Input : [1, 2, 4, 6, 7, 9, 10]
Output : [3, 5, 8]

"""
# below order of o(n^2) because every number it is transeversing all the array
# It is multiple number missing this only approach
def find_missing(lst):
    ans = []
    for i in range(1, lst[-1]):   #
        if i not in lst:
            ans.append(i)
    return ans

lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))

# For single number missing
# if index + 1 is not matching with it content return

def find_missing(lst):
    for i in range(len(lst)):
        if i + 1 != lst[i]:
            return i + 1

lst = [1,2,3,4,6,7,8]
print(find_missing(lst))

# for unsorted array
# take sum of n seqence number n(n+1)/2 - sum(len)
# o(n)  because of sum
#
def find_missing(lst):
    n = max(lst)       # max of important because unsorted array we don't where is 
    tot = n*(n+1)/2
    s = sum(lst)
    mis = tot - s
    return mis

lst = [1,2,3,4,6,7,8]
print(find_missing(lst))


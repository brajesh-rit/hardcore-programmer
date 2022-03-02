"""
https://www.geeksforgeeks.org/allocate-minimum-number-pages/
Given number of pages in n different books and m students. The books are arranged in ascending order of number of pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that the maximum number of pages assigned to a student is minimum.
Example :


Input : pages[] = {12, 34, 67, 90}
        m = 2
Output : 113
Explanation:
There are 2 number of students. Books can be distributed
in following fashion :
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student
      2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student
      2 with 67 + 90 = 157 pages
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student
      1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113.
successful run in geeksof geeks
"""

class Solution:
    def isPossible(self, arr, n, m, curr_min):
        studentsRequired = 1
        curr_sum = 0

        # iterate over all books
        for i in range(n):

            # check if current number of pages are
            # greater than curr_min that means
            # we will get the result after
            # mid no. of pages
            if (arr[i] > curr_min):
                return False

            # count how many students are required
            # to distribute curr_min pages
            if (curr_sum + arr[i] > curr_min):

                # increment student count
                studentsRequired += 1

                # update curr_sum
                curr_sum = arr[i]

                # if students required becomes greater
                # than given no. of students, return False
                if (studentsRequired > m):
                    return False

            # else update curr_sum
            else:
                curr_sum += arr[i]

        return True


    # function to find minimum pages
    def findPages(self, arr, n, m):

        # return -1 if no. of books is
        # less than no. of students
        if (n < m):
            return -1

        # Count total number of pages
        Total = sum(arr)

        # initialize start as 0 pages and
        # end as total pages
        start = max(arr)
        end =  Total
        result = float('inf')

        # traverse until start <= end
        while (start <= end):

            # check if it is possible to distribute
            # books by using mid as current minimum
            mid = start + (end - start) // 2
            if (self.isPossible(arr, n, m, mid)):

                # update result to current distribution
                # as it's the best we have found till now.
                result = mid

                # as we are finding minimum and books
                # are sorted so reduce end = mid -1
                # that means
                end = mid - 1

            else:
                # if not possible means pages should be
                # increased so update start = mid + 1
                start = mid + 1

        # at-last return minimum no. of pages
        return result


# Driver Code

# Number of pages in books
arr = [12, 34, 67, 90]
n = len(arr)
m = 2  # No. of students
result = Solution()
print("Minimum number of pages = ",
      result.findPages(arr, n, m))

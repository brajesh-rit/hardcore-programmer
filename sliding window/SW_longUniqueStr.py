"""
https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.


Example 1:

Input:
S = "aabacbebebe", K = 3
Output: 7
Explanation: "cbebebe" is the longest
substring with K distinct characters.
"""

class Solution:
    def longestKSubstr(self, str, k):
        leng = len(str)
        start = 0
        end = 0
        ch = {}
        ans = -1
        while end < leng:
            try:
              ch[str[end]] += 1
            except KeyError:
                ch[str[end]] = 1
            dlen = len(ch)
            if dlen < k:
                None
            elif dlen == k:
                ans = max(ans, (end - start + 1))
            elif dlen > k:
                while dlen > k:
                    ch[str[start]] -= 1
                    if ch[str[start]] == 0:
                        del(ch[str[start]])
                    dlen = len(ch)
                    start += 1
            end += 1
        return ans

test = Solution()
str = "aabacbebebe"
k = 3
print(test.longestKSubstr(str,3))
str = "aaaa"
k = 2
print(test.longestKSubstr(str,3))
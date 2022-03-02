"""
https://leetcode.com/problems/minimum-window-substring/
Minimum Window Substring
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""
class Solution(object):
    def minWindow(self, str, txt):
        if str == txt:
            return str
        leng = len(str)
        start = 0
        end = 0
        ans = []
        out = float('inf')
        map = dict.fromkeys(txt,0)
        for ch in txt:
            map[ch] += 1
        ind = len(map)
        while end < leng:
            try:
                map[str[end]] -= 1
                if map[str[end]] == 0:
                    ind -= 1
            except KeyError:
                None
            if ind == 0:
                while ind == 0:
                    try:
                        map[str[start]] += 1
                        if map[str[start]] > 0:
                            ind += 1
                            if out > (end - start + 1):
                                out = (end - start + 1)
                                ans = [start, end]
                    except KeyError:
                        None
                    start += 1
            end += 1
        if len(ans) > 0:
            res = str[ans[0]: ans[1]+1]
        else:
            res = ""
            print("empty")
        return res

test = Solution()
str = "ADOBECODEBANC"
txt = "ABC"
print(test.minWindow(str,txt))
str = "a"
txt = "aa"
print(test.minWindow(str,txt))
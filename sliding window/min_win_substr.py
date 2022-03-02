"""
#https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

class Solution(object):
    def minWindow(self, s, t):
        
        start = 0
        end = 0
        out = 0
        map = {}
        map = dict.fromkeys(t,0)  # fromkeys is not inline function it returns pointer hence I use dict
        for ch in t:
            map[ch] = map[ch] + 1
        tot = count = len(map)
        strLen = len(s)
        while end < strLen:
            if count > 0:
                try:
                    map[s[end]] = map[s[end]] - 1
                    if map[s[end]] == 0:
                        count = count - 1
                except KeyError:
                    None
                if count > 0:
                    end = end + 1
            elif count == 0:
                #try to minimize the window
                while count <= 0:
                    try:
                        map[s[start]] = map[s[start]] + 1
                        if map[s[start]] == 1 and count == 0:
                            if out == 0:
                                out = end - start + 1
                            else:
                                out = min(out, end - start + 1)
                            count = count + 1
                            end = end + 1
                        start = start + 1
                    except KeyError:
                        None
                        start += 1
        return  out


    def minWindow1(self, s, t):
        #https://leetcode.com/problems/minimum-window-substring/
        start = 0
        end = 0
        out = float('inf')  # intialize with maximum value
        output = ""
        result = False
        map = {}
        if len(t) > len(s):
            return output
        map = dict.fromkeys(t,0)  # fromkeys is not inline function it returns pointer hence I use dict
        for ch in t:
            map[ch] = map[ch] + 1
        count = len(map)
        strLen = len(s)
        while end < strLen:
            if count > 0:
                try:
                    map[s[end]] = map[s[end]] - 1
                    if map[s[end]] == 0:
                        count = count - 1
                except KeyError:
                    None
                if count > 0:
                    end = end + 1
            elif count == 0:
                #try to minimize the window
                while count <= 0:
                    try:
                        map[s[start]] = map[s[start]] + 1
                        if map[s[start]] == 1 and count == 0:
                            out = min(out, end - start + 1)
                            result = True
                            count = count + 1
                            end = end + 1
                        start = start + 1
                    except KeyError:
                        None
                        start += 1
        if count == len(map) and not result:
            if s == t:
                return t
            else:
                return ""
        output = s[start-1:end+1]
        return  output



result = Solution()
print(result.minWindow1('ABAACBAB', 'ABC'))
print(result.minWindow1('ADOBECODEBANC', 'ABC'))
print(result.minWindow1('a', 'a'))
print(result.minWindow1('a', 'aa'))
print(result.minWindow1('a', 'b'))
print(result.minWindow1('ab', 'a'))
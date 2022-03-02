"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
class Solution(object):
    def lengthOfLongestSubstring(self, str):
        leng = len(str)
        start, end, ans = 0,0,0
        ch = {}
        while end < leng:
            try:
                ch[str[end]] += 1
            except KeyError:
                ch[str[end]] = 1
            dleng = len(ch)
            wleng = end - start + 1
            if wleng < dleng:
                None
            elif wleng == dleng:
                ans = max(ans,wleng)
            elif wleng > dleng:
                while wleng > dleng:
                    ch[str[start]] -= 1
                    if ch[str[start]] == 0:
                        del(ch[str[start]])
                    dleng = len(ch)
                    start += 1
                    wleng = end - start + 1
            end += 1
        return ans

test = Solution()
str = "pwwkew"
print(test.lengthOfLongestSubstring(str))

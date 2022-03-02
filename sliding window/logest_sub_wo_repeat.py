class Solution:
    def lengthOfLongestSubstring(self, s):
        end = 0
        start = 0
        ch = {}
        max_win = 0
        while end <len(s):
            try:
                ch[s[end]] = ch[s[end]] + 1
            except KeyError:
                ch[s[end]] = 1
            cnt = len(ch)
            if cnt == end - start + 1:
                max_win = max(max_win, cnt)
                end = end + 1
            elif cnt < end - start + 1:
                while cnt < end - start + 1:
                    ch[s[start]] = ch[s[start]]  - 1
                    if ch[s[start]] == 0:
                        del ch[s[start]]
                    cnt = len(ch)
                    start = start + 1
                end = end + 1
        return max_win

result = Solution()
print (result.lengthOfLongestSubstring( 'abcabcbb'))
print (result.lengthOfLongestSubstring( 'bbbbb'))
print (result.lengthOfLongestSubstring( 'pwwkew'))
print (result.lengthOfLongestSubstring( ''))

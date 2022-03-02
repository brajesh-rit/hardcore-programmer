class Solution:
    def longestKSubstr(self, s, k):
        end = 0
        start = 0
        ch = {}
        max_win = -1
        while end <len(s):
            try:
                ch[s[end]] = ch[s[end]] + 1
            except KeyError:
                ch[s[end]] = 1
            cnt = len(ch)
            if cnt < k:
                end = end + 1
            elif cnt == k:
                max_win = max(max_win, end - start + 1)
                end = end + 1
            elif cnt > k:
                while cnt > k:
                    ch[s[start]] = ch[s[start]]  - 1
                    if ch[s[start]] == 0:
                        del ch[s[start]]
                    cnt = len(ch)
                    start = start + 1
                end = end + 1
        return max_win

result = Solution()
print (result.longestKSubstr( 'aabacbebebe',3))
print (result.longestKSubstr( 'aaaa',2))
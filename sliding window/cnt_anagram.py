class Solution:
    #https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1#
    def search(self, pat, txt):
        pat_cnt =dict.fromkeys(pat,0)   # intialization must be required before pattern count
        for ch in pat:
            pat_cnt[ch] =  pat_cnt[ch] + 1  #  pat_cnt {'a': 3, 'b': 2, 'c': 5}
        match = len(pat_cnt)
        start = 0
        end = 0
        out = 0
        while(end != len(pat)):
            if txt[end] in pat_cnt:
                pat_cnt[txt[end]] = pat_cnt[txt[end]] - 1
                if pat_cnt[txt[end]] == 0:
                    match = match - 1
                if match == 0:
                    out = out + 1
            end = end + 1
        end = end - 1
        while(end != len(txt)-1):
            if txt[start] in pat_cnt:
                pat_cnt[txt[start]] = pat_cnt[txt[start]] + 1
                if pat_cnt[txt[start]] == 1:
                    match = match + 1
            start = start + 1
            end = end + 1
            if txt[end] in pat_cnt:
                pat_cnt[txt[end]] = pat_cnt[txt[end]] - 1
                if pat_cnt[txt[end]] == 0:
                    match = match - 1
                if match == 0:
                    out = out + 1
        return out
    #https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/  accept
    def findAnagrams(self, txt, pat):
        if len(pat) > len(txt):     # assumed pattern length is less than txt length
            return []
        pat_cnt =dict.fromkeys(pat,0)   # intialization must be required before pattern count
        for ch in pat:
            pat_cnt[ch] =  pat_cnt[ch] + 1  #  pat_cnt {'a': 3, 'b': 2, 'c': 5}
        match = len(pat_cnt)
        start = 0
        end = 0
        out = []
        len_pat = len(pat)
        while(end != len_pat):
            if txt[end] in pat_cnt:   #  first check charcter present in dictionary or not
                pat_cnt[txt[end]] = pat_cnt[txt[end]] - 1
                if pat_cnt[txt[end]] == 0:
                    match = match - 1
                if match == 0:
                    out.append(end - len_pat + 1)
            end = end + 1
        end = end - 1
        while(end != len(txt)-1):
            if txt[start] in pat_cnt:
                pat_cnt[txt[start]] = pat_cnt[txt[start]] + 1
                if pat_cnt[txt[start]] == 1:
                    match = match + 1
            start = start + 1
            end = end + 1
            if txt[end] in pat_cnt:
                pat_cnt[txt[end]] = pat_cnt[txt[end]] - 1
                if pat_cnt[txt[end]] == 0:
                    match = match - 1
                if match == 0:
                    out.append(end - len_pat + 1)
        return out

result = Solution()
print (result.findAnagrams( 'forxxorfxdofr','for'))
print (result.findAnagrams( 'aabaabaa','aaba'))

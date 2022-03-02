"""
https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
Count Occurences of Anagrams
Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

Example 1:

Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.
"""
class Solution:
    def search(self, pat, txt):
        leng = len(txt)
        patDict = dict.fromkeys(pat,0)
        for ch in pat:
            patDict[ch] += 1
        start = 0
        end = 0
        ans = 0
        pleng = len(pat)
        match = len(patDict)
        while end < leng:
            if txt[end] in patDict:
                patDict[txt[end]] -= 1
                if patDict[txt[end]] == 0:
                    match -= 1
            if (end - start + 1) == pleng:
                if match == 0:
                    ans += 1
                if txt[start] in patDict:
                    if patDict[txt[start]] == 0:
                        match += 1
                    patDict[txt[start]] += 1
                start += 1
            end += 1
        return ans

test = Solution()
# txt = 'forxxorfxdofr'
# pat = 'for'
txt = 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
pat = 'kkkkk'
print(test.search(pat,txt))
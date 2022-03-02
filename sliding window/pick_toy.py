'''John is at a toy store help him pick maximum number of toys. He can only select in a
   continuous manner and he can select only K =2types of toys
   Example:
   Input:
        1
         abaccab
'''
class Solution:
    def pickToy(self, s, k):
        start = 0
        end = 0
        out = 0
        map = {}
        lnMap = 0
        while end < len(s):
            try:
                map[s[end]] = map[s[end]] + 1
            except:
                map[s[end]] = 1
            lnMap = len(map)
            if lnMap < k:
                end = end + 1
            elif lnMap == k:
                out = max(out,end - start + 1)
                end = end + 1
            elif lnMap > k:
                while lnMap > k:
                    map[s[start]] = map[s[start]] - 1
                    if map[s[start]] == 0:
                        del(map[s[start]])
                        lnMap = len(map)
                    start = start + 1
                end = end + 1
        return  out

result = Solution()
print (result.pickToy( 'abaccab', 2))
print (result.pickToy( 'abaccaaaaaaaacb', 2))
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # str convert integer to string
        s = str(abs(x))
        # s[::-1] shortcut for reverse the string
        rev = s[::-1]
        # int() function is for conversion of string to integer
        res = int(rev)
        if x < 0 :
            res = res * - 1
        if abs(res) > 2147483647:
           res = 0
        return res

result = Solution()
print (result.reverse( - 1234))
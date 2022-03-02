class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0:
            return False
        seg_arr = []
        while x !=0:
            x , y = x//10 , x % 10
            seg_arr.append(y)
        return seg_arr == seg_arr[::-1]


result = Solution()

#print (result.isPalindrome(121))
print (result.isPalindrome(-1231))

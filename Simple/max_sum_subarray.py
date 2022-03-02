class Solution(object):
    def maxSumArray(self, arr, size):
        sum = 0
        maxVal = 0
        for start in range(len(arr)-1):
            for val in range(size):
                sum = sum + arr[start + val]
            maxVal =  max(maxVal, sum)
            sum = 0
        return  maxVal

    def maxSumArray2(self, arr, size):
        """
        :type x: int
        :rtype: bool
        """
        start = 0
        end = 0
        sum = 0
        arrLength = len(arr)
        while(end - start + 1) <= size:  #window size is (end - start + 1)
            sum = sum + arr[end]
            end = end + 1
        maxVal = sum
        while end < arrLength:
            sum = sum - arr[start]
            sum = sum + arr[end]
            end = end + 1
            start = start + 1
            maxVal = max(maxVal,sum)
        return  maxVal


result = Solution()
print (result.maxSumArray2([100, 200, 300, 400], 2))


class Solution(object):
    """def twoSum(self, nums, target):

        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        for first in nums:
            sec = target - first
            if sec in nums:
                output = [nums.index(first), nums.index(sec)]    # This program has bug nums = [3,3], target =6
                if nums.index(first) == nums.index(sec):
                    continue
                else:
                    return output


       def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):          #take array of tuple of (index and values)
            remaining = target - num            #stores remain values
            if remaining in values:             # simple check remain is present or not i)if present then retrun both the index  (this is bug when same value first itself ( [3,3] target = 6)
                return [i, values[remaining]]    # rectify this store the index in dictionary where value as index (this is help implement unique hash map of index
            else:
                values[num] = i


       def twoSum(self, nums, target):
           for i in range(len(nums)):
               for j in range(i+1, len(nums)):
                   if nums[i]+nums[j]==target:
                       return i,j

    def twoSum(self, nums, target):
         for i, num in enumerate(nums):
            for j, item in enumerate(nums):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


    def twoSum(self, nums, target):
       leng = len(nums)
       for i in range(leng):
           firstNum = nums[i]                  #store first number
           for j in range(leng):
               if i != j and (nums[j] == target - firstNum):    #again go through the array see the remain value is match with array but avoid the index same
                   return [i, j]

    label = -1
    def twoSum(self, nums, target):
        if target == 0:
            return [self.label]
        for i, val in enumerate(nums):
            self.label = self.label + 1
            output = self.twoSum(nums[1:], target - val)
            self.label = self.label - 1
            if self.label != -1:
                return output + [self.label]  # append change the value in memory
            else:
                return output         # At the end root automatically add 0
"""
    def twoSum(self,nums, target):
        for i , val in enumerate(nums):     #Since collecting index hence first get index and value both
            second = target - val           #collect the remaining value and again search index against it
            try :
                ind_sec = nums.index(second)   # value not found in array
            except ValueError:
                continue
            if i != ind_sec:
                return [i,ind_sec]


result = Solution()
#print (result.twoSum( [2,7,11,15], 9))
print (result.twoSum( [3,2,3], 6))
#print (result.twoSum( [3,3], 6))
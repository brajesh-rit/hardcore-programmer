#https://leetcode.com/problems/scramble-string/
#We can scramble a string s to get a string t using the following algorithm:

#1. If the length of the string is 1, stop.
#2. If the length of the string is > 1, do the following:
#       Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
#       Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
#       Apply step 1 recursively on each of the two substrings x and y.
#Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
#

class Solution:
    def isScramble1(self, s1, s2):

        #checking if all characters of s1 are in s2
        if sorted(s1)!=sorted(s2):
           return False
        #if s1 <4 less than three length string is easily achieveable by ordering or else if strings are equal then also we can conclude it
        if len(s1)<4 or s1==s2:
            return True

        f=self.isScramble   #Here rename the function and calling it
        #checking each combination of strings if they match return True
        for i in range(1,len(s1)):
                # swap not happen                            swap happen
            if f(s1[:i],s2[:i]) and f(s1[i:],s2[i:]) or f(s1[:i],s2[-i:]) and f(s1[i:],s2[:-i]):
                return True
        return False



    mem={}
    def isScramble(self, s1, s2):
        #checking if (s1,s2) already in dictionary or not
        #Here we can use key as a set
        if (s1,s2) in self.mem:
            return self.mem[(s1,s2)]
        #checking if all characters of s1 are in s2
        if sorted(s1)!=sorted(s2):
            self.mem[(s1,s2)]=False
            return False
        #if s1 <4 less than three length string is easily achieveable by ordering or else if strings are equal then also we can conclude it
        if len(s1)<4 or s1==s2:
            self.mem[(s1,s2)]=True
            return True
        f=self.isScramble
        #checking each combination of strings if they match return True
        for i in range(1,len(s1)):
            if f(s1[:i],s2[:i]) and f(s1[i:],s2[i:]) or f(s1[:i],s2[-i:]) and f(s1[i:],s2[:-i]):
                return True
        self.mem[(s1,s2)]=False
        return False

result = Solution()
s1 = "great"
s2 = "rgeat"
print(result.isScramble(s1,s2))
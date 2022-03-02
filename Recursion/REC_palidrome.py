def ispalindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return ispalindrome(word[1:-1])

str = 'abcbaew'
if ispalindrome(str):
    print (str+" is a palidrom")
else:
    print(str + " is not a palidrom")
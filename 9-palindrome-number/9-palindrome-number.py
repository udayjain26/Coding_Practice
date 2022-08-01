class Solution:
    def isPalindrome(self, x: int) -> bool:
        revStr = str(x)[::-1]
        if revStr == str(x):
            return True
        else:
            return False
                
        
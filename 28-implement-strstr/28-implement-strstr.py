class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            result = haystack.index(needle)
            return result
        except:
            return -1
        
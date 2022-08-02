class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for char in s:
            encountered = ""
            counter = 0
            for char in s:
                if char in encountered:
                        s = s[1:]
                        break
                else:
                    counter+=1
                    encountered+=char
            if counter > maxLen:
                maxLen = counter
        return maxLen
        
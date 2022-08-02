class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        lcpf = ""
        smallestStr = min(strs, key = len)
        
        for pos, char in enumerate(smallestStr):
            check = True
            
            for string in strs:
                if string[pos] != char:
                    check = False
                    break
                    
            if check:
                lcpf += char
            else:
                break
                
        return lcpf
                
                
                
            
                
            
        
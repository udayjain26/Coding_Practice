class Solution:
    def isValid(self, s: str) -> bool:
        bracketList = []
        if len(s) % 2 != 0:
            return False
        
        b1C = 0
        b2C = 0
        b3C = 0
        
        for c in s:
            if c == "(":
                bracketList.append(c)
                b1C +=1 
            if c =="[":
                bracketList.append(c)
                b2C +=1
            if c == "{":
                bracketList.append(c)
                b3C +=1
                
            if c == ")":
                b1C -= 1
                if b1C < 0:
                    return False
                if bracketList and bracketList.pop() != "(":
                    return False
                
            elif c == "]":
                b2C -= 1
                if b2C < 0:
                    return False
                if bracketList and bracketList.pop() != "[":
                    return False
            
            elif c == "}":
                b3C -= 1
                if b3C < 0:
                    return False
                if bracketList and bracketList.pop() != "{":
                    return False
                
        if b1C != 0 or b2C != 0 or b3C !=0:
            return False
        
        return True
        
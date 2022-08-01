class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        counter = 0
        strlen = len(s) - 1
        
        while counter <= strlen:
            
            print(counter, strlen, sum)
            if s[counter] == "M":
                sum+=1000
                counter+=1
                continue
                
            elif s[counter] == "D":
                sum+=500
                counter+=1
                continue
                
            elif s[counter] == "C" and counter+1<=strlen:
                if s[counter+1] == "D":
                    sum+=400
                    counter +=2
                    continue
                elif s[counter+1] == "M":
                    sum+=900
                    counter +=2
                    continue
                    
            if s[counter] == "C":
                sum+=100
                counter +=1
                continue
                
            elif s[counter] == "L":
                sum+=50
                counter +=1
                continue
                
                
            elif s[counter] == "X" and counter+1<=strlen:
                if s[counter+1] == "L":
                    sum+=40
                    counter +=2
                    continue
                    
                elif s[counter+1] == "C":
                    sum+=90
                    counter +=2
                    continue
                    
            if s[counter] == "X":
                sum+=10
                counter+=1
                continue
                
            if s[counter] == "V":
                sum+=5
                counter+=1
                continue
            

            elif s[counter] == "I" and counter+1<=strlen:
                if s[counter+1] == "V":
                    sum+=4
                    counter +=2
                    continue
                    
                elif s[counter+1] == "X":
                    sum+=9
                    counter +=2
                    continue
            
            if s[counter] == "I":
                sum+=1
                counter +=1
                continue
        return sum    
        
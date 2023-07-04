class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s.split():
            if i in "{[(":
                a.append(i)                    
            if i in "])}":
                    if i ==  "}":
                              try:
                                        a.remove("}")
                              except:
                                        continue
                    elif i == "]":
                              try:
                                        a.remove("]")
                              except:
                                        continue
                    elif i ==  ")":
                              try:
                                        a.remove(")")
                              except:
                                        continue
                    else:
                              continue

                    
        if len(a)==0:
            print("true")
        else:
            print("false")


            
s = Solution()
s.isValid("{}))")

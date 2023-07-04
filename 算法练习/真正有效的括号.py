class Solution:
    def isValid(self, s):
        d = []
        balanced = True
        index = 0
        while index < len(s) and balanced:
            a = s[index]
            if a in "({[":
                d.append(a)
            else:
                if len(d) == 0:
                    balanced = False
                else:
                    top = d.pop()
                    if not self.maches(top, a):
                        balanced = False

                        
            index = index + 1
        if balanced and d == []:
                return True
        else:
                return False
    def maches(self,openq,close):
        opens = "([{"
        closes = ")]}"
        return opens.index(openq)==closes.index(close)


s = Solution()
if s.isValid("{})))"):
          print("true")
else:
          print("false")


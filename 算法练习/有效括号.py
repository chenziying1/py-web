s = "([)]"

'''
stack = [0,0,0]
for i in s:
          if i == '(' : 
                    stack[0] += 1
          if i == '{' :
                    stack[1] += 1
          if i == '[':
                    stack[2] += 1
          if i == ')':
                    stack[0] -= 1
          if i == '}':
                    stack[1] -= 1
          if i == ']':
                    stack[2] -= 1
        
ans = sum(stack)
if ans > 0:
          print( 'False')
else:
          print('True')
'''



stack = []
for i in s:
          if i == '(' or i == '{' or i == '[':
                    stack.append(i)
          else:
                    a = stack.pop()
                    if i == ')' and a != '(':
                              print( 'False')
                    if i == '}' and a != '{':
                              print( 'False')
                    if i == ']' and a != '[':
                              print('False')
ans = len(stack)
if ans == 0:
          print('True')
else:
          print('False')



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if i == ')' and a != '(':
                            return False
                if i == '}' and a != '{':
                            return False
                if i == ']' and a != '[':
                            return False
        ans = len(stack)
        if ans == 0:
            return True
        else:
            return False
                              

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        pmap = {')':'(', '}':'{', ']':'['}

        for i in s: 
            if i in pmap: 
                if stack and stack[-1] == pmap[i]:
                    stack.pop() 
                else:
                    return False 
                
            else:
                stack.append(i)

        return True if not stack else False 
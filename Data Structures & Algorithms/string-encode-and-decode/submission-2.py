class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            length = len(i)
            res += (str(length) + '#' + i)
        
        return res 

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 

        while i < len(s):
            markPos = i 
            while s[markPos] != '#':
                markPos += 1 
            
            length = int(s[i:markPos])
            word = str(s[markPos+1:markPos+1+length])
            res.append(word)

            i = markPos+1+length

        return res 

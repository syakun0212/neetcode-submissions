class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)

        for i in range(len(s2) - len(s1) + 1):
            word = s2[i:i+len(s1)]
            c = Counter(word)
            if c == s1c:
                return True
        return False 
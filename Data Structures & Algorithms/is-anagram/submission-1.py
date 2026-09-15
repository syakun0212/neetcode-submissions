class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s = Counter(s)
        c_t = Counter(t)

        return (c_s == c_t)
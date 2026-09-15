class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for word in strs:
            c = [0] * 26
            for i in word:
                c[ord(i) - ord('a')] += 1 
            res[tuple(c)].append(word)
        
        return list(res.values())




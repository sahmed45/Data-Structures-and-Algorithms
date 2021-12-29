class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for word in strs:
            anagramId = ''.join(sorted(word))
            if anagramId in anagramMap:
                anagramMap[anagramId].append(word)
            else:
                anagramMap[anagramId] = [word]
        return list(anagramMap.values())
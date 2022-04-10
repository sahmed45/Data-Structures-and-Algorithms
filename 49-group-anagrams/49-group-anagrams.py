class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            anagram_id = ''.join(sorted(word))
            if anagram_id in anagram_map:
                anagram_map[anagram_id].append(word)
            else:
                anagram_map[anagram_id] = [word]
        return list(anagram_map.values())
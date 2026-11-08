class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for st in strs : 
            anagrams["".join(sorted(st))].append(st)
        
        return [val for _, val in anagrams.items()]


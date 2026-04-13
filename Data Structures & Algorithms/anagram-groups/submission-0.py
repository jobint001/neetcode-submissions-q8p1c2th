class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 ={}

        for word in strs:
            s=tuple(sorted(word))
            if s in dict1:
                dict1[s].append(word)
            else:
                dict1[s]=list()
                dict1[s].append(word)
        
        result = list()
        for key1,word in dict1.items():
            result.append(word)

        return result
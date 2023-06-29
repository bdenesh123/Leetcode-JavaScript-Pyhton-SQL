from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = defaultdict(list)
        result =[]

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_dict[sorted_s].append(s)

        for value in anagram_dict.values():
            result.append(value)

        return result      



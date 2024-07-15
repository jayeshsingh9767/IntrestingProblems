class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create Map of sorted string with the actual string and return list of map values
        anagram_map = defaultdict(list)
        for i in strs:
            a = "".join(sorted(i))
            anagram_map[a].append(i)

        return list(anagram_map.values())

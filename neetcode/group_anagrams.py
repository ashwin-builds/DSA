# MAIN IDEAS:
# 1. Use a character count array using index for the count and value as the character
# 2. Convert to tuple for hashing because you can't hash a list in python

# Time: O(m + n) -> m is the length of each word, n is the number of words
# Space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            character_count_arr = [0] * 26 # for 26 unique letters
            for char in word:
                character_count_arr[ord(char) - ord("a")] += 1 # the ord func subtracts ascii values
            
            character_count_arr = tuple(character_count_arr)
            if character_count_arr in res.keys():
                res[character_count_arr].append(word)
            else:
                res[character_count_arr] = [word]

        return list(res.values())
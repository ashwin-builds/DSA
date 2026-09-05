# Time: O(n * m) -> where n is num of words in arr and m is length of shorest word in arr
# Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # find shorest word to prevent index out of bounds error
        min_length = float('inf')
        for word in strs:
            if len(word) < min_length:
                min_length = len(word)

        i = 0

        while i < min_length:
            for word in strs:
                if word[i] != strs[0][i]:
                    return word[:i]
            i += 1

        # if the condition never fails, we need to return 
        return word[:i]

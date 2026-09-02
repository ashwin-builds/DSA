# Time: O(A + B) -> loop through both words
# Space: O(A + B) -> list of size A + B

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        A = len(word1)
        B = len(word2)
        a, b = 0, 0
        s = []
        word = 1 # flips between 1 and 2

        while a < A and b < B:
            if word == 1:
                s.append(word1[a])
                a += 1
                word = 2
            elif word == 2:
                s.append(word2[b])
                b += 1
                word = 1

        while a < A:
            s.append(word1[a])
            a += 1

        while b < B:
            s.append(word2[b])
            b += 1

        return ''.join(s) # Time: O(A + B), Space: O(A + B)

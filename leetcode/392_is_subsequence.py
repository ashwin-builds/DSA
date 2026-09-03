# Time: O(T) -> length of full string
# Space: O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        S = len(s)
        T = len(t)
        # some special cases:
        if S > T: # substring bigger than actual string 
            return False
        if S == 0: # empty substring is a valid substring
            return True

        s_index = 0

        for t_index in range(T):
            if s[s_index] == t[t_index]:
                if s_index == S - 1:
                    return True
                s_index += 1

        return False

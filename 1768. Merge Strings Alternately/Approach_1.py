class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i = 0
        j = 0
        list_soln = []
        while i <= len(word1) or j <= len(word2):
            if i == len(word1) and j == len(word2):
                return "".join(list_soln)
            else:
                if i < len(word1):
                    list_soln.append(word1[i])
                    i += 1

                if j < len(word2):
                    list_soln.append(word2[j])
                    j += 1
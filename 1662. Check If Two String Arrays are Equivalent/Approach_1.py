class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        word_1 = "".join(word1)
        word_2 = "".join(word2)
        if word_1 == word_2:
            return True
        else:
            return False
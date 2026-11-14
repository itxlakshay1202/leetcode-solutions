class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        si = 0 
        ei = len(letters) - 1

        if ord(target) < ord(letters[si]) or ord(target) >= ord(letters[ei]):
            return letters[0]

        while si < ei:
            mid = si + (ei - si) // 2

            if ord(letters[mid]) <= ord(target):
                si = mid+1
            else:
                ei = mid

        return letters[si]
        
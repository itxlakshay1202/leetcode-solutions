class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        user = 1
        while True:
            if x < 1 or y < 4:
                if user == 1:
                    return "Bob"
                else:
                    return "Alice"

            else:
                if user == 1:
                    user += 1
                else:
                    user -= 1
                x -= 1
                y-=4
        
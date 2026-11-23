class Solution(object):
    def operation(self,n):
        i = 0
        num = []
        while i <= len(n) -2:
            sum = n[i] + n[i+1]
            num.insert(0,sum % 10)
            i+=1
        return num

    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        l = []
        while i < len(s):
            l.append(int(s[i]))
            i+=1

        while len(l) != 2:
            l = self.operation(l)

        if l[0] == l[1]:
            return True
        else:
            return False
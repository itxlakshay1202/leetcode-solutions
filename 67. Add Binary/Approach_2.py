class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        i = 0
        num_a = 0
        num_b = 0
        while i < len(a):
            p = len(a)-i-1
            if a[i] == '1':
                num_a += pow(2,p)
            i+=1
         
        i = 0
        while i < len(b):
            p = len(b)-i-1
            if b[i] == '1':
                num_b += pow(2,p)
            i+=1
        print(num_a)
        print(num_b)
        num_sum = num_a+num_b
        if num_sum == 0:
            return "0"
        while num_sum > 0:
            if num_sum % 2 == 0:
                res.insert(0,'0')
            else:
                res.insert(0,'1')

            num_sum //= 2

        return "".join(res)
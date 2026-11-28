class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0
        lst = []
        try:
            while True:
                dic = {}
                for j in strs:
                    if j[i] not in dic and len(dic) == 0:
                        dic[j[i]] = 1
                    elif j[i] not in dic:
                        return "".join(lst)
                    else:
                        dic[j[i]] += 1
                lst.append(j[i])
                i+=1

        except:
            return "".join(lst)
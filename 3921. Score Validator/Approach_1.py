class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        i = 0
        score = [0,0]
        while i < len(events):
            if events[i] == "W":
                score[1] += 1
                if score[1] == 10:
                    break
            else:
                if events[i] == "2":
                    score[0] += 2
                elif events[i] == "3":
                    score[0] += 3
                elif events[i] == "4":
                    score[0] += 4
                elif events[i] == "6":
                    score[0] += 6
                elif events[i] == "0":
                    score[0] += 0
                else:
                    score[0] += 1
            i+=1

        return score
        
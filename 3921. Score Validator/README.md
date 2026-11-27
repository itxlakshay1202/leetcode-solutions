# 3921. Score Validator

### Difficulty: Easy

## Description
You are given a string array events.

Initially, score = 0 and counter = 0. Each element in events is one of the following:


	"0", "1", "2", "3", "4", "6": Add that value to the total score.
	"W": Increase the counter by 1. No score is added.
	"WD": Add 1 to the total score.
	"NB": Add 1 to the total score.


Process the array from left to right. Stop processing when either:


	All elements in events have been processed, or
	The counter becomes 10.


Return an integer array [score, counter], where:


	score is the final total score.
	counter is the final counter value.


 
Example 1:


Input: events = ["1","4","W","6","WD"]

Output: [12,1]

Explanation:


	
		
			Event
			Score
			Counter
		
		
			"1"
			1
			0
		
		
			"4"
			5
			0
		
		
			"W"
			5
			1
		
		
			"6"
			11
			1
		
		
			"WD"
			12
			1
		
	


Final result: [12, 1].


Example 2:


Input: events = ["WD","NB","0","4","4"]

Output: [10,0]

Explanation:


	
		
			Event
			Score
			Counter
		
		
			"WD"
			1
			0
		
		
			"NB"
			2
			0
		
		
			"0"
			2
			0
		
		
			"4"
			6
			0
		
		
			"4"
			10
			0
		
	


Final result: [10, 0].


Example 3:


Input: events = ["W","W","W","W","W","W","W","W","W","W","W"]

Output: [0,10]

Explanation:

After 10 occurrences of "W", the counter reaches 10, so processing stops. The remaining events are ignored.


 
Constraints:


	1 <= events.length <= 1000
	events[i] is one of "0", "1", "2", "3", "4", "6", "W", "WD", or "NB".

## Submission Details
- **Status**: Accepted
- **Runtime**: 6
- **Memory**: 12396000
- **Language**: python

## Code
```python
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
        
```

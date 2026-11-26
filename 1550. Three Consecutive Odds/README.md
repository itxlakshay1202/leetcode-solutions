# 1550. Three Consecutive Odds

### Difficulty: Easy

## Description
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 
Example 1:


Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.


Example 2:


Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


 
Constraints:


	1 <= arr.length <= 1000
	1 <= arr[i] <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 13
- **Memory**: 12360000
- **Language**: python

## Code
```python
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        while i <= len(arr) - 3:
            print(i)
            if arr[i] % 2 == 1:
                if arr[i+1] % 2 == 1:
                    if arr[i+2] % 2 == 1:
                        return True
                    else:
                        i+=3
                else:
                    i+= 2
            else:
                i+=1
        return False
```

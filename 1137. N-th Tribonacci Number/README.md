# 1137. N-th Tribonacci Number

### Difficulty: Easy

## Description
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 
Example 1:


Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4


Example 2:


Input: n = 25
Output: 1389537


 
Constraints:


	0 <= n <= 37
	The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 11924000
- **Language**: python

## Code
```python
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = [0,1,1]
        i = 3
        while i <= n:
            lst.append(lst[i-1] + lst[i-2] + lst[i-3])
            i+=1

        return lst[n]
```

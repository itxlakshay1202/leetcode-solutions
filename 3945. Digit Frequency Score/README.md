# 3945. Digit Frequency Score

### Difficulty: Easy

## Description
You are given an integer n.

The score of n is defined as the sum of d * freq(d) over all distinct digits d, where freq(d) denotes the number of times the digit d appears in n.

Return an integer denoting the score of n.

 
Example 1:


Input: n = 122

Output: 5

Explanation:


	The digit 1 appears 1 time, contributing 1 * 1 = 1.
	The digit 2 appears 2 times, contributing 2 * 2 = 4.
	Thus, the score of n is 1 + 4 = 5.



Example 2:


Input: n = 101

Output: 2

Explanation:


	The digit 0 appears 1 time, contributing 0 * 1 = 0.
	The digit 1 appears 2 times, contributing 1 * 2 = 2.
	Thus, the score of n is 2.



 
Constraints:


	1 <= n <= 109

## Submission Details
- **Status**: Accepted
- **Runtime**: 1
- **Memory**: 12000000
- **Language**: python

## Code
```python
class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        while n > 0:
            lst.append(n%10)
            n//=10
        sum = 0
        for i in range(0,10):
            sum += i * lst.count(i)

        return sum
```

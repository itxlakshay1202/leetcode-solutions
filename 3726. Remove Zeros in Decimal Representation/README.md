# 3726. Remove Zeros in Decimal Representation

### Difficulty: Easy

## Description
You are given a positive integer n.

Return the integer obtained by removing all zeros from the decimal representation of n.

 
Example 1:


Input: n = 1020030

Output: 123

Explanation:

After removing all zeros from 1020030, we get 123.


Example 2:


Input: n = 1

Output: 1

Explanation:

1 has no zero in its decimal representation. Therefore, the answer is 1.


 
Constraints:


	1 <= n <= 1015

## Submission Details
- **Status**: Accepted
- **Runtime**: 3
- **Memory**: 12232000
- **Language**: python

## Code
```python
class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        count = 0
        while n > 0:
            if n% 10 != 0:
                num = n % 10 * (10 ** count) + num
                count += 1
            n//= 10
        return num
```

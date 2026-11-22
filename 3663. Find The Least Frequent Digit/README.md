# 3663. Find The Least Frequent Digit

### Difficulty: Easy

## Description
Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.

Return the chosen digit as an integer.
The frequency of a digit x is the number of times it appears in the decimal representation of n.
 
Example 1:


Input: n = 1553322

Output: 1

Explanation:

The least frequent digit in n is 1, which appears only once. All other digits appear twice.


Example 2:


Input: n = 723344511

Output: 2

Explanation:

The least frequent digits in n are 7, 2, and 5; each appears only once.


 
Constraints:


	1 <= n <= 231​​​​​​​ - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 20
- **Memory**: 12236000
- **Language**: python

## Code
```python
class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic ={}
        while n > 0:
            if n % 10 not in dic:
                dic[n%10] = 1
            else:
                dic[n%10] += 1
            n //= 10
        
        m = min(dic.values())
        print(dic)
        for k in sorted(dic):
            if dic[k] == m:
                return k
```

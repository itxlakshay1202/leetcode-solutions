# 2180. Count Integers With Even Digit Sum

### Difficulty: Easy

## Description
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.

 
Example 1:


Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    


Example 2:


Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.


 
Constraints:


	1 <= num <= 1000

## Submission Details
- **Status**: Accepted
- **Runtime**: 8
- **Memory**: 12048000
- **Language**: python

## Code
```python
class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        while num != 0:
            sum = 0
            num_cpy = num
            while num_cpy > 0:
                sum += num_cpy % 10
                num_cpy //= 10
            if sum % 2 == 0:
                count += 1
            num -= 1
        return count
```

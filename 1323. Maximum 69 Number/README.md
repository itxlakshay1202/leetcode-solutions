# 1323. Maximum 69 Number

### Difficulty: Easy

## Description
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 
Example 1:


Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.


Example 2:


Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.


Example 3:


Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.


 
Constraints:


	1 <= num <= 104
	num consists of only 6 and 9 digits.

## Submission Details
- **Status**: Accepted
- **Runtime**: 0 ms
- **Memory**: 12072000
- **Language**: python

## Code
```python
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = []
        while num > 0:
            lst.insert(0,num % 10)
            num = num // 10

        i = 0
        while i < len(lst):
            if lst[i] == 6:
                lst[i] = 9
                break
            else:
                i += 1

        res = 0
        for i in lst :
            res = res * 10 + i

        return res
```

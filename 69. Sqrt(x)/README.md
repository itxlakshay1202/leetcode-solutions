# 69. Sqrt(x)

### Difficulty: Easy

## Description
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.


	For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


 
Example 1:


Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.


Example 2:


Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


 
Constraints:


	0 <= x <= 231 - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 7
- **Memory**: 12192000
- **Language**: python

## Code
```python
class Solution(object):
    def mySqrt(self, x):
        if x== 1:
            return 1
        si = 0
        ei = x
        while si <= ei:
            if si == ei:
                return si
            else:
                mid = si + (ei - si) // 2

                if mid * mid == x:
                    return mid
                elif mid * mid < x:
                    if mid == si:
                        return si
                    else:
                        si = mid
                else:
                    if mid == ei:
                        return ei
                    else:
                        ei = mid
```

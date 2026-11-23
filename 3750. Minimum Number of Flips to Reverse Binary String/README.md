# 3750. Minimum Number of Flips to Reverse Binary String

### Difficulty: Easy

## Description
You are given a positive integer n.

Let s be the binary representation of n without leading zeros.

The reverse of a binary string s is obtained by writing the characters of s in the opposite order.

You may flip any bit in s (change 0 → 1 or 1 → 0). Each flip affects exactly one bit.

Return the minimum number of flips required to make s equal to the reverse of its original form.

 
Example 1:


Input: n = 7

Output: 0

Explanation:

The binary representation of 7 is "111". Its reverse is also "111", which is the same. Hence, no flips are needed.


Example 2:


Input: n = 10

Output: 4

Explanation:

The binary representation of 10 is "1010". Its reverse is "0101". All four bits must be flipped to make them equal. Thus, the minimum number of flips required is 4.


 
Constraints:


	1 <= n <= 109

## Submission Details
- **Status**: Accepted
- **Runtime**: 9
- **Memory**: 12128000
- **Language**: python

## Code
```python
class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = []
        while n > 0:
            lis.insert(0,n % 2)
            n //= 2
        
        flip = 0
        si = 0
        ei = len(lis)-1
        while si <= ei:
            if lis[si] != lis[ei]:
                flip += 2
            si += 1
            ei -= 1
            
        return flip
```

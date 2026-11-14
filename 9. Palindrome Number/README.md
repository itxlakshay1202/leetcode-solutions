# 9. Palindrome Number

### Difficulty: Easy

## Description
Given an integer x, return true if x is a palindrome, and false otherwise.

 
Example 1:


Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Example 2:


Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


Example 3:


Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


 
Constraints:


	-231 <= x <= 231 - 1


 
Follow up: Could you solve it without converting the integer to a string?

## Submission Details
- **Status**: Accepted
- **Runtime**: 5
- **Memory**: 45992000
- **Language**: java

## Code
```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;          // negatives are never palindromes
        if (x != 0 && x % 10 == 0) return false; // e.g. 10, 100 (but not 0)

        int original = x;
        long reversed = 0;                // long avoids overflow on reversal
        while (x > 0) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }

        return reversed == original;
    }
}
```

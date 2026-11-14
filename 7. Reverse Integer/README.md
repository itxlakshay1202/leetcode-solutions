# 7. Reverse Integer

### Difficulty: Medium

## Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:


Input: x = 123
Output: 321


Example 2:


Input: x = -123
Output: -321


Example 3:


Input: x = 120
Output: 21


 
Constraints:


	-231 <= x <= 231 - 1

## Submission Details
- **Status**: Accepted
- **Runtime**: 13
- **Memory**: 42956000
- **Language**: java

## Code
```java
class Solution {
    public int reverse(int x) {
        int soln = 0;
        if(x > 0){
        while (x > 0){
            if(soln > 214748364.7){
                return 0;
            }
            soln = soln*10 + x%10;
            System.out.println(soln);
            x /= 10;
        }
        }else{
            x = -x;
            while (x > 0){
                if(soln > 214748364.8){
                    return 0;
                }
            soln = soln*10 + x%10;
            x /= 10;
            }
            soln = -soln;
        }
            return soln;
    }
}
```

# 345. Reverse Vowels of a String

### Difficulty: Easy

## Description
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 
Example 1:


Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


Example 2:


Input: s = "leetcode"

Output: "leotcede"


 
Constraints:


	1 <= s.length <= 3 * 105
	s consist of printable ASCII characters.

## Submission Details
- **Status**: Accepted
- **Runtime**: 1
- **Memory**: 9520000
- **Language**: c

## Code
```c
char* reverseVowels(char* s) {
    int size = strlen(s) / sizeof(char);
    int si = 0;
    int ei = size -1;
    while(si < ei){
        if (s[ei] != 'a' && s[ei] != 'e' && s[ei] != 'i' && s[ei] != 'o' && s[ei] != 'u' && s[ei] != 'A' && s[ei] != 'E' && s[ei] != 'I' && s[ei] != 'O' && s[ei] != 'U'){
            ei--;
            continue;
        }else if (s[si] == 'a' || s[si] == 'e' || s[si] == 'i' || s[si] == 'o' || s[si] == 'u' || s[si] == 'A' || s[si] == 'E' || s[si] == 'I' || s[si] == 'O' || s[si] == 'U'){
            char temp = s[si];
            s[si] = s[ei];
            s[ei] = temp;
            ei--;
        }

        si++;
    }

    return s;
}
```

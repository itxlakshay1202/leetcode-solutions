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
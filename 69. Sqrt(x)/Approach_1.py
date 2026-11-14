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
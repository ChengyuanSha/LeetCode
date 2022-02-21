import re


def mySqrt(x: int) -> int:
    low, high = 0, x
    while high >= low:
        mid = int(low + (high - low) / 2)
        power = mid * mid
        if power > x:
            high = mid - 1
        elif power < x:
            low = mid + 1
        else:  # mid * mid == x or high == low:
            return mid
    return high



print(mySqrt(8))
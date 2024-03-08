def sq(num):
  s = 0
  e = num
  ans = -1
  while s <= e:
    mid = s + (e-s)//2
    square = mid * mid
    if square == num:
        return mid
    elif square < num:
        ans = mid
        s = mid + 1
    else:
        e = mid -1
  return ans    

class Solution:
    def mySqrt(self, x: int) -> int:
        return sq(x)

        
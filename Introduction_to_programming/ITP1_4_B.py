import math

r = float(input())

# 累乗で記述し、 Runtime Error.
# 素直に変数を二回積算する方法の方が早い
print(r*r*math.pi, 2.0*math.pi*r)
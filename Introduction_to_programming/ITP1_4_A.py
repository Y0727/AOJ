a, b = map(int, input().split())

# float型の小数点以下の位数の指定方法を調べた
print("%d %d %.10f"%(a/b, a%b, a/b))
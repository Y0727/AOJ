a, b, c = map(int, input().split())

# for文を書き忘れて一度不正解に
for i in range(3):
    if a > b:
        a, b = b, a
    elif b > c:
        b, c = c, b
    elif a > b:
        a, b = b, a

print(a, b, c)